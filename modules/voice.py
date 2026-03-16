import threading  
import speech_recognition as sr  
import pyttsx3
from queue import Queue 


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

def speak(text: str, wait=True):  
    if not text:
        return
    if wait:  
        engine.say(text)  
        engine.runAndWait()  
    else:  
        speak_queue.put(text)  

def listen(timeout=15):  
    recognizer = sr.Recognizer()  
    #sensitivity adjustments
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:  
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  
        print("listening...")  
        try:  
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=10)  
        except sr.WaitTimeoutError:  
            return None  
    try:    
        command = recognizer.recognize_google(audio)    
        print(f"you said {command}")    
        return command.lower()    
    except sr.UnknownValueError:    
          
        return None    
    except sr.RequestError:    
        print("Network Error : I couldn't connect to speech services")    
        return None
