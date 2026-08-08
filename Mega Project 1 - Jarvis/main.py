import sounddevice as sd
import numpy as np
import wave
import io
import os
import re
import tempfile
import speech_recognition as sr
import webbrowser
import musicLibrary
import requests
from gtts import gTTS
import pygame
from openai import OpenAI
from datetime import datetime

weatherApi = "<API>"  # add open-meteo api
newsApi = "<API>"     # add newsapi.org api
groqApi = "<API>"  # add your groq api key here

recognizer = sr.Recognizer()
pygame.mixer.init()

SAMPLE_RATE = 16000

CAPABILITIES = [
    ('"Jarvis, open <site>"', "Opens a website from your saved list (urls.txt)"),
    ('"Jarvis, play <song>"', "Plays a song from your music library"),
    ('"Jarvis, what\'s the news"', "Reads the top 5 headlines"),
    ('"Jarvis, what time is it"', "Tells the current time"),
    ('"Jarvis, search <query>"', "Searches Google for you"),
    ('"Jarvis, weather in <city>"', "Gives current weather (defaults to Dhaka)"),
    ("Anything else", "Falls back to AI for a general answer"),
]


def printWelcome():
    print("=" * 55)
    print("  JARVIS - Voice Assistant")
    print("=" * 55)
    print("Say \"Jarvis\" to wake me up, then give a command.\n")
    print("Here's what I can do:")
    for command, description in CAPABILITIES:
        print(f"  • {command:<32} -> {description}")
    print("=" * 55)


# ---------------- Speech cleanup ----------------
def clean_for_speech(text):
    """Strip markdown so TTS doesn't read out '*', '#', etc, and collapse it
    into short flowing sentences instead of long bullet lists."""
    text = re.sub(r'[*_#`]', '', text)
    text = re.sub(r'^\s*[-•]\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n+', '. ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()


# ---------------- Audio: Speak  ----------------
def speak(text):
    text = clean_for_speech(text)
    if not text:
        return

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        path = f.name

    try:
        tts = gTTS(text=text, lang='en')
        tts.save(path)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(0)
        pygame.mixer.music.unload()
    finally:
        if os.path.exists(path):
            os.remove(path)


# ---------------- Audio: Listen ----------------
def record_audio(duration, fs=SAMPLE_RATE):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return audio


def to_audio_data(audio, fs=SAMPLE_RATE):
    buf = io.BytesIO()
    with wave.open(buf, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())
    buf.seek(0)
    with sr.AudioFile(buf) as source:
        return recognizer.record(source)


def listen(duration=4):
    print("Listening....")
    audio = record_audio(duration)
    audio_data = to_audio_data(audio)
    try:
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print("API error:", e)
        return ""


# ---------------- AI Fallback ----------------
def aiProcess(command):
    client = OpenAI(
        api_key=groqApi,
        base_url="https://api.groq.com/openai/v1"
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a voice assistant. You are being read aloud by "
                    "text-to-speech, so you MUST answer in at most 2-3 short spoken "
                    "sentences. Never use markdown, bullet points, asterisks, headers, "
                    "or numbered lists. Speak plainly like a person talking, not writing. "
                    "If the question needs code, briefly say so and keep the explanation "
                    "to one short sentence."
                ),
            },
            {
                "role": "user",
                "content": command
            }
        ],
        temperature=0.7,
        max_tokens=120,
    )

    return response.choices[0].message.content


def getCurrentTime():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    print(f"The current time is {current_time}")
    speak(f"The current time is {current_time}")


def loadWebUrls(filename="urls.txt"):
    urls = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line or ":" not in line:
                    continue
                name, url = line.split(":", 1)  # split only on first ':'
                urls[name.strip().lower()] = url.strip()
    except FileNotFoundError:
        print(f"{filename} not found, no sites loaded.")
    return urls


def searchGoogle(c):
    query = c.replace("search", "").strip()
    if query:
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        speak("Please specify what you want to search for.")


def getWeather(city="Dhaka"):
    try:
        r = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
        data = r.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        feels = current["FeelsLikeC"]
        humidity = current["humidity"]
        desc = current["weatherDesc"][0]["value"]

        print(
            f"1. The weather in {city} is {desc}. ", "\n"
            f"2. The temperature is {temp} degrees Celsius, ", "\n"
            f"3. feels like {feels} degrees, ", "\n"
            f"4. and humidity is {humidity} percent."
        )
        speak(
            f"The weather in {city} is {desc}. "
            f"The temperature is {temp} degrees Celsius, "
            f"feels like {feels} degrees, "
            f"and humidity is {humidity} percent."
        )

    except Exception as e:
        print(e)
        speak("Sorry, I couldn't get the weather.")


def getNews():
    try:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApi}", timeout=5
        )

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            if not articles:
                speak("Sorry, I couldn't find any news.")
                return

            titles = [a.get("title", "No title") for a in articles[:5]]
            for i, title in enumerate(titles, start=1):
                print(f"{i}. {title}")

            # Speak all headlines in ONE tts call instead of 6 separate ones
            speak("Here are the top headlines. " + ". ".join(titles))

        else:
            speak("Sorry, I couldn't fetch the news.")

    except Exception as e:
        print(e)
        speak("An error occurred while fetching the news.")


def playMusic(command):
    song = command.replace("play", "").strip().lower()

    for name, url in musicLibrary.music.items():
        if song in name:
            speak(f"Playing {name}")
            webbrowser.open(url)
            return

    speak(f"Sorry, I don't have {song} in my music library.")


def openWebsite(url):
    webbrowser.open(url)


def processCommand(c):
    print("Processing command:", c)

    c = c.lower()

    # ---------- Open Websites ----------
    if c.startswith("open"):
        for name, url in site_urls.items():
            if name in c:
                speak(f"Opening {name}")
                openWebsite(url)
                return

        speak("Site not found in my list.")
        return

    # ---------- Play Music ----------
    if c.startswith("play"):
        playMusic(c)
        return

    # ---------- Get News ----------
    if "news" in c:
        getNews()
        return

    # ---------- Get Time ----------
    if "time" in c:
        getCurrentTime()
        return

    # ---------- Search Google ----------
    if "search" in c:
        searchGoogle(c)
        return

    # ---------- Weather ----------
    if "weather" in c:
        city = "Dhaka"

        if "in" in c:
            city = c.split("in", 1)[1].strip()

        getWeather(city)
        return

    # -------------- AI -------------
    else:
        output = aiProcess(c)
        print(output)
        speak(output)


site_urls = loadWebUrls()

if __name__ == "__main__":
    printWelcome()
    speak("Initializing Jarvis.")

    while True:
        try:
            # ------------------ WAIT FOR WAKE WORD ------------------
            wake_word = listen(duration=3).lower()
            if not wake_word:
                continue

            print("Heard:", wake_word)

            if "jarvis" not in wake_word:
                continue

            speak("Yes?")

            # ------------------ ACTIVE MODE ------------------
            while True:
                command = listen(duration=4)

                if not command:
                    print("No command. Going to sleep...")
                    speak("Going to sleep.")
                    break

                print("Command:", command)
                processCommand(command)
                # Timer automatically resets because we loop again.

        except KeyboardInterrupt:
            print("Exiting Jarvis...")
            break

        except Exception as e:
            print("Error:", e)