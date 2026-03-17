import threading
import speech_recognition as sr
import pyttsx3
import queue
import os
import sys
import ctypes
import psutil
import pyautogui
import pyjokes
import pywhatkit
import google.generativeai as genai
from duckduckgo_search import DDGS
from datetime import datetime

# ── 1. CONFIGURATION & BRAIN ──────────────────────────────
API_KEY = "YOUR_GEMINI_API_KEY"  # 🚩 Insert your API key here
genai.configure(api_key=API_KEY)

class SAMGenerativeBrain:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.chat = self.model.start_chat(history=[])
        self.identity = (
            "You are SAM-V1, the first-generation AI created by Ayush. "
            "You are witty, loyal, and sound like a DedSec operative. "
            "Keep your answers concise and cool. If you can't do a task, "
            "just respond conversationally as a friend."
        )

    def think(self, user_input):
        try:
            prompt = f"{self.identity}\nUser: {user_input}"
            response = self.chat.send_message(prompt)
            return response.text
        except Exception as e:
            print(f"Brain Error: {e}")
            return "My neural links are flickering, sir. But I am still here."

# ── 2. TTS ENGINE (THREADED) ──────────────────────────────
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

speak_queue = queue.Queue()

def speaker_loop():
    while True:
        text = speak_queue.get()
        if text is None: break
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("TTS error", e)
        finally:
            speak_queue.task_done()

threading.Thread(target=speaker_loop, daemon=True).start()

def speak(text: str, wait=True):
    if not text: return
    if wait:
        engine.say(text)
        engine.runAndWait()
    else:
        speak_queue.put(text)

# ── 3. SPEECH RECOGNITION ────────────────────────────────
def listen(timeout=15):
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
            command = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {command}")
            return command.lower()
        except Exception:
            return None

# ── 4. FUNCTIONAL MODULES ────────────────────────────────
def system_control(command):
    if "battery" in command or "status" in command:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            charging = "charging" if battery.power_plugged else "not charging"
            speak(f"Your system battery is at {percent} percent and it is {charging}")
    elif "lock" in command:
        speak("Locking your system now.")
        ctypes.windll.user32.LockWorkStation()
    elif "volume up" in command:
        speak("Increasing volume")
        for _ in range(5): pyautogui.press("volumeup")
    elif "volume down" in command:
        speak("Decreasing volume")
        for _ in range(5): pyautogui.press("volumedown")

def web_ops(command):
    if "play" in command:
        speak("playing on youtube")
        pywhatkit.playonyt(command.replace("play", "").strip())
    elif "search" in command:
        query = command.replace("search for", "").replace("look up", "").strip()
        speak(f"searching the web for {query}")
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=2))
            if results:
                speak(results[0]["body"])

def handle_apps(command):
    app_commands = {
        "open notepad": lambda: os.startfile("notepad.exe"),
        "open calculator": lambda: os.startfile("calc.exe"),
        "open chrome": lambda: os.startfile("chrome.exe"),
        "open vscode": lambda: os.startfile(r"D:\Microsoft VS Code\Code.exe")
    }
    for app in app_commands:
        if app in command:
            speak(f"Opening {app.replace('open ', '')}")
            app_commands[app]()
            return True
    return False

# ── 5. MAIN ORCHESTRATOR ─────────────────────────────────
if __name__ == "__main__":
    brain_instance = SAMGenerativeBrain()
    speak("All systems online, sir.")

    while True:
        command = listen(timeout=15)
        if command is None: continue

        command = command.lower().strip()

        # 1. EXIT
        if "exit" in command or "quit" in command:
            speak("Systems offline. Stay safe, sir.")
            sys.exit()

        # 2. APPS
        if handle_apps(command):
            continue

        # 3. SYSTEM
        elif any(word in command for word in ["battery", "status", "lock", "volume"]):
            system_control(command)

        # 4. FUN & INFO
        elif "joke" in command:
            speak(pyjokes.get_joke())
        elif "time" in command:
            speak(f"The current time is {datetime.now().strftime('%H:%M')}")
        elif "date" in command:
            speak(f"Todays date is {datetime.today().strftime('%B %d, %Y')}")
        elif "screenshot" in command:
            try:
                pyautogui.screenshot("screenshot.png")
                speak("Screenshot saved as screenshot.png")
            except:
                speak("I couldn't take a screenshot")

        # 5. WEB
        elif "play" in command or "search" in command:
            web_ops(command)

        # 6. GENERATIVE BRAIN
        else:
            if len(command) > 1:
                print("🧠 Routing to Gemini...")
                ai_reply = brain_instance.think(command)
                print(f"SAM: {ai_reply}")
                speak(ai_reply)