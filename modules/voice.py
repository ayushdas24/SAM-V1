import threading  
import speech_recognition as sr  
import pyttsx3
from queue import Queue 
from modules.config import MIC_DEVICE_INDEX


#1.Initialize the TTS Engine properly
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

speak_queue = Queue()


def speaker_loop():  
    while True:  
        text = speak_queue.get()  
        if text is None:  
            break  
        try:  
            engine.say(text)  
            engine.runAndWait()  
        except Exception as e:  
            print("TTS error", e)  
        finally:
            speak_queue.task_done()

threading.Thread(target=speaker_loop, daemon=True).start()  

def speak(text: str):
    """Non-blocking. queues text to be spoken in background"""
    if text:
        speak_queue.put(text)

def speak_now(text: str):
    """Blocking. speaks immediately, waits until done.
       Use this for boot messages and shutdown confirmation"""
    if text:
        engine.say(text)
        engine.runAndWait()

def listen_for_wake_word(wake_word: str) -> bool:
    """
    Short 3-second listen window.
    Returns True if wake word detected, False otherwise.
    Called in a tight loop - stays CPU-light because of short timeout.
    """
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True

    try:
        with sr.Microphone(device_index=MIC_DEVICE_INDEX) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

        text = recognizer.recognize_google(audio).lower()
        print(f"[Passive] Heard: {text}")

        wake_word = ["sam", "samm", "sammy", "sum"]
        words = text.split()

        if any(word in text for word in wake_word):
            print("[passive] wake word detected!")
            return True

    except sr.WaitTimeoutError:
        pass             #normal silence during pssive listening
    except sr.UnknownValueError:
        pass             #Normal - background noise
    except sr.RequestError:
        print("[voice] Network error- speech service unreachable.")
    except Exception as e:
        print(f"[Passive listen Error] {e}")

    return False

def listen_for_command() -> str | None:
    """
    Activated after wake word is detected.
    Longer window - gives user time to speak a full command
    Returns the spoken command as Lowercase string, or None.
    """
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True

    try:
        with sr.Microphone(device_index=MIC_DEVICE_INDEX) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("[SAM] Ready - speak your command...")

            audio = recognizer.listen(source, timeout=10 , phrase_time_limit=8)

        command = recognizer.recognize_google(audio).lower().strip()
        print(f"[command] You said: {command}")
        return command
    
    except sr.WaitTimeoutError:
        speak("I don't hear anything, Sir.")
        return None
    except sr.UnknownValueError:
        speak("couldn't catch that.")
        return None
    except sr.RequestError:
        speak("speech services is offline")
        return None
    except Exception as e:
        print(f"[command listen Error] {e}")
        return None