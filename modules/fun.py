import pyjokes
import pyautogui
from datetime import datetime
from modules.voice import speak

def tell_jokes():
    joke = pyjokes.get_joke()
    print(f"[fun] joke: {joke}")
    speak(joke)
    return joke

def get_time():
    now = datetime.now()
    time_str = now.strftime("%H:%M")
    return time_str

def tell_time():
    time_str = get_time()
    print(f"[fun] time is {time_str}")
    speak(f"The current time is {time_str}")
    return time_str

def get_date():
    return datetime.now().strftime("%B %d, %Y")
    

def tell_date():
    date_str = get_date()
    print(f"[fun] Date is {date_str}")
    speak(f"today's date is {date_str}")
    return date_str

def take_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        file_path = "screenshot.png"
        screenshot.save(file_path)
        speak("screenshot taken and saved as screenshot.png")
        return f"screenshot saved at {file_path}"
    except Exception as e:
        print("screenshot failed:",e)
        speak("sorry i couldn't take the screenshot")
        return f"screenshot failed: {e}"