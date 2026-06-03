import pyjokes
import pyautogui
from datetime import datetime
from modules.voice import speak

def tell_jokes(should_speak=True):
    joke = pyjokes.get_joke()
    print(f"[fun] joke: {joke}")
    if should_speak:
        speak(joke)
    return joke

def get_time():
    now = datetime.now()
    time_str = now.strftime("%H:%M")
    return time_str

def tell_time(should_speak=True):
    time_str = get_time()
    print(f"[fun] time is {time_str}")

    if should_speak:
        speak(f"The current time is {time_str}")
        
    return time_str

def get_date():
    return datetime.now().strftime("%B %d, %Y")
    

def tell_date(should_speak=True):
    date_str = get_date()
    print(f"[fun] Date is {date_str}")

    if should_speak:
        speak(f"today's date is {date_str}")
    return date_str

def take_screenshot(should_speak=True):
    try:
        screenshot = pyautogui.screenshot()
        file_path = "screenshot.png"
        screenshot.save(file_path)
        if should_speak:
            speak("screenshot taken and saved as screenshot.png")
        return f"screenshot saved at {file_path}"
    except Exception as e:
        print("screenshot failed:",e)
        if should_speak:
            speak("sorry i couldn't take the screenshot")
        return f"screenshot failed: {e}"