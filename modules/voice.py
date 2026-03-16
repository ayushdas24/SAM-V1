import threading  
import speech_recognition as sr  
from modules.config import engine, speak_queue  

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

threading.Thread(target=speaker_loop, daemon=True).start()  

def speak(text: str, wait=True):  
    if wait:  
        engine.say(text)  
        engine.runAndWait()  
    else:  
        speak_queue.put(text)  

def listen(timeout=15):  
    recognizer = sr.Recognizer()  
    with sr.Microphone() as source:  
        recognizer.adjust_for_ambient_noise(source, duration=1)  
        print("listening...")  
        try:  
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=timeout)  
        except sr.WaitTimeoutError:  
            return None  
    try:    
        command = recognizer.recognize_google(audio)    
        print(f"you said {command}")    
        return command.lower()    
    except sr.UnknownValueError:    
        speak("I could not understand. please say it again.")    
        return None    
    except sr.RequestError:    
        speak("I couldn't connect to speech services.")     
        return None
