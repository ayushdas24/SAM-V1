import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import pyautogui
import os
import threading
import queue
import ctypes
import psutil
from duckduckgo_search import DDGS
from datetime import datetime

# ── TTS ENGINE ──────────────────────────────────────────
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

speak_queue = queue.Queue()

def speaker_loop():
    while True:
        text = speak_queue.get()
        if text is None:
            break
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("TTS error:", e)

threading.Thread(target=speaker_loop, daemon=True).start()

def speak(text: str, wait=True):
    if wait:
        engine.say(text)
        engine.runAndWait()
    else:
        speak_queue.put(text)

# ── SPEECH RECOGNITION ──────────────────────────────────
def listen(timeout=15):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=timeout)
        except sr.WaitTimeoutError:
            return None
    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("I could not understand. Please say it again.")
        return None
    except sr.RequestError:
        speak("I couldn't connect to speech services.")
        return None

# ── SYSTEM COMMANDS ─────────────────────────────────────
def shutdown():
    speak("Shutting down your system in 10 seconds. Please save your work.")
    os.system("shutdown /s /t 10")

def restart():
    speak("Restarting your system in 10 seconds. Please save your work.")
    os.system("shutdown /r /t 10")

def lock_system():
    speak("Locking your system now.")
    ctypes.windll.user32.LockWorkStation()

def system_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        charging = "charging" if battery.power_plugged else "not charging"
        speak(f"Your system battery is at {percent} percent and it is {charging}")
    else:
        speak("Sorry, I couldn't fetch battery information.")

def volume_up():
    speak("Increasing volume")
    for _ in range(5):
        pyautogui.press("volumeup")

def volume_down():
    speak("Decreasing volume")
    for _ in range(5):
        pyautogui.press("volumedown")

def mute_volume():
    speak("Muting volume")
    pyautogui.press("volumemute")

# ── WEB ─────────────────────────────────────────────────
def search_web(query):
    try:
        query = query.replace("search for", "").replace("look up", "").strip()
        if query:
            speak(f"Searching the web for {query}")
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=2))
                if results:
                    answer = results[0]["body"]
                    print("Results:", answer)
                    speak(answer)
                else:
                    speak("Sorry, I couldn't find anything on that.")
    except Exception as e:
        print("Search error:", e)
        speak("Something went wrong while searching.")

def youtube_play(query):
    speak("Playing on YouTube")
    pywhatkit.playonyt(query.replace("play", "").strip())

def google_search(query):
    speak("Searching in Google")
    pywhatkit.search(query)

# ── FUN ─────────────────────────────────────────────────
def tell_jokes():
    joke = pyjokes.get_joke()
    speak(joke)

def tell_time():
    now = datetime.now()
    speak(f"The current time is {now.strftime('%H:%M')}")

def tell_date():
    today = datetime.today()
    speak(f"Today's date is {today.strftime('%B %d, %Y')}")

def take_screenshot():
    try:
        speak("Taking a screenshot")
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot saved as screenshot.png")
    except Exception as e:
        print("Screenshot error:", e)
        speak("I couldn't take a screenshot")

# ── APP LAUNCHER ─────────────────────────────────────────
app_commands = {
    "open notepad": lambda: os.startfile("notepad.exe"),
    "open calculator": lambda: os.startfile("calc.exe"),
    "open chrome": lambda: os.startfile("chrome.exe"),
    "open vscode": lambda: os.startfile(r"D:\Microsoft VS Code\Code.exe")
}

# ── MAIN LOOP ────────────────────────────────────────────
speak("All systems online, sir. How may I assist?")

while True:
    command = listen(timeout=15)

    if command is None:
        speak("I didn't hear anything. Can you say that again?")
        continue

    if "exit" in command or "quit" in command:
        speak("Goodbye! Stay safe sir.")
        break

    executed = False
    for app in app_commands:
        if app in command:
            try:
                speak(f"Opening {app.replace('open ', '')}")
                app_commands[app]()
            except Exception:
                speak(f"Sorry, {app.replace('open ', '')} could not be opened.")
            executed = True
            break

    if executed: continue

    if "shutdown" in command: shutdown(); continue
    if "restart" in command: restart(); continue
    if "lock" in command: lock_system(); continue
    if "battery" in command or "status" in command: system_status(); continue
    if "volume up" in command: volume_up(); continue
    if "volume down" in command: volume_down(); continue
    if "mute" in command: mute_volume(); continue
    if "search for" in command or "look up" in command: search_web(command); continue
    if "play" in command: youtube_play(command); continue
    if "search" in command: google_search(command); continue
    if "screenshot" in command: take_screenshot(); continue
    if "joke" in command or "joker" in command: tell_jokes(); continue
    if "time" in command: tell_time(); continue
    if "date" in command: tell_date(); continue

    speak("Sorry, I couldn't do that.")

