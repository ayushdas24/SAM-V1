import pyjokes  
import pyautogui  
from datetime import datetime  
from modules.voice import speak  

def tell_jokes():  
    joke = pyjokes.get_joke()  
    speak(joke)  

def tell_time():  
    now = datetime.now()  
    current_time = now.strftime("%H:%M")  
    speak(f"The current time is {current_time}")  

def tell_date():  
    today = datetime.today()  
    date_str = today.strftime("%B %d, %Y")  
    speak(f"Todays date is {date_str}")  

def take_screenshot():  
    try:  
        speak("Take a screenshot")  
        screenshot = pyautogui.screenshot()  
        screenshot.save("screenshot.png")  
        speak("Screenshot saved as screenshot.png")  
    except Exception as e:  
        print("Screenshot error:", e)  
        speak("I couldn't take a screenshot")