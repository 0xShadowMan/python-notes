# Jarvis — Voice Assistant

A Python voice assistant with wake-word activation, speech recognition, text-to-speech, and an AI fallback for general questions. Built without PyAudio or pyttsx3 — uses `sounddevice` for recording and `gTTS` + `pygame` for speech output.

## Features

| Command | Description |
|---|---|
| `Jarvis, open <site>` | Opens a website from your saved list (`urls.txt`) |
| `Jarvis, play <song>` | Plays a song from your music library |
| `Jarvis, what's the news` | Reads the top 5 headlines |
| `Jarvis, what time is it` | Tells the current time |
| `Jarvis, search <query>` | Searches Google for you |
| `Jarvis, weather in <city>` | Gives current weather (defaults to Dhaka) |
| Anything else | Falls back to an AI model for a general answer |

Say **"Jarvis"** to wake it up, then speak your command. If no command is heard for a few seconds, it goes back to sleep and waits for the wake word again.

## How it works

- **Speech-to-text:** Records short audio clips with `sounddevice`, converts them to `AudioData`, and transcribes with `SpeechRecognition` (Google Web Speech API).
- **Text-to-speech:** Generates speech with `gTTS` and plays it back with `pygame`.
- **AI fallback:** Any command that isn't matched to a specific action is sent to an LLM (via the Groq API, OpenAI-compatible endpoint) and the response is read aloud.
- Markdown/formatting is stripped from AI responses before speaking, and the system prompt keeps answers short and speech-friendly.

## Requirements

- Python 3.10+

## Installation

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install sounddevice numpy gTTS pygame SpeechRecognition requests openai
```

## Configuration

This project needs three API keys:

| Key | Used for | Get it from |
|---|---|---|
| `weatherApi` | Reserved for future use with [OpenWeatherMap](https://openweathermap.org) | [openweathermap.org](https://openweathermap.org) |
| `newsApi` | Top headlines | [newsapi.org](https://newsapi.org) |
| `groqApi` | AI fallback answers | [console.groq.com](https://console.groq.com) |

In `main.py`, the keys are set as placeholders:

```python
weatherApi = "<API>"  # add open-meteo api
newsApi = "<API>"     # add newsapi.org api
groqApi = "<API>"     # add your groq api key here
```

Replace `<API>` with your own keys to run the script.

## Setup (Optional)

This repo already includes `urls.txt` and `musicLibrary.py` — edit them to add your own sites and songs.

- `urls.txt` — one entry per line, used by the "open" command:
   ```
   github: https://github.com
   youtube: https://youtube.com
   ```
- `musicLibrary.py` — a `music` dict mapping song names to URLs, used by the "play" command:
   ```python
   music = {
       "song name": "https://youtube.com/watch?v=..."
   }
   ```

Run it:
   ```bash
   python main.py
   ```

## Notes

- Speech recognition uses Google's free Web Speech API through the `SpeechRecognition` library — it requires an internet connection.
- `gTTS` also requires an internet connection to generate speech.
- This project is for personal/educational use. Respect the terms of service of any APIs used.