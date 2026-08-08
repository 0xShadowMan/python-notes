#!/usr/bin/env python3

import time
import datetime
import sys
import os


def beep():
    """Play a sound / beep. Works cross-platform with fallbacks."""
    try:
        # Try system bell first (works in most terminals)
        for _ in range(5):
            print("\a", end="", flush=True)
            time.sleep(0.5)
    except Exception:
        pass

    # Try platform-specific sound as a stronger alert
    if sys.platform.startswith("linux"):
        os.system("paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga 2>/dev/null "
                   "|| aplay /usr/share/sounds/alsa/Front_Center.wav 2>/dev/null")
    elif sys.platform == "darwin":
        os.system("afplay /System/Library/Sounds/Glass.aiff")
    elif sys.platform == "win32":
        import winsound
        for _ in range(5):
            winsound.Beep(1000, 500)


def get_alarm_time():
    while True:
        alarm_str = input("Set alarm time (HH:MM, 24-hour format): ").strip()
        try:
            alarm_time = datetime.datetime.strptime(alarm_str, "%H:%M").time()
            return alarm_time
        except ValueError:
            print("Invalid format. Please use HH:MM, e.g. 07:30")


def wait_for_alarm(alarm_time):
    print(f"\nAlarm set for {alarm_time.strftime('%H:%M')}. Waiting...")
    print("Press Ctrl+C to cancel.\n")

    try:
        while True:
            now = datetime.datetime.now().time()
            current_str = now.strftime("%H:%M:%S")
            print(f"\rCurrent time: {current_str}", end="", flush=True)

            if now.hour == alarm_time.hour and now.minute == alarm_time.minute and now.second == 0:
                print("\n\n⏰ WAKE UP! Alarm ringing! ⏰")
                beep()
                break

            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nAlarm cancelled.")


def main():
    print("=== Simple Alarm Clock ===")
    alarm_time = get_alarm_time()
    wait_for_alarm(alarm_time)


if __name__ == "__main__":
    main()
