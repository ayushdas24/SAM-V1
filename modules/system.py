import os  
import ctypes  
import psutil  
import pyautogui  
from modules.voice import speak  

def shutdown():  
    speak("shutting down your system in 10 seconds. please save your work")  
    os.system("shutdown /s /t 10")  

def restart():  
    speak("Restarting your system in 10 seconds.")  
    os.system("shutdown /r /t 10")  

def lock_system():  
    speak("Locking your system now.")  
    ctypes.windll.user32.LockWorkStation()  

def system_status():  
    battery = psutil.sensors_battery()  
    if battery:  
        percent = battery.percent  
        charging = "charging" if battery.power_plugged else "not charging"  
        speak(f"your system battery is at {percent} percent and it is {charging}")  
    else:  
        speak("Sorry, i couldn't fetch battery information.")  

def volume_up():  
    speak("Increasing volume")  
    for _ in range(5):  
        pyautogui.press("volumeup")  

def volume_down():  
    speak("decreasing volume")  
    for _ in range(5):  
        pyautogui.press("volumedown")  

def mute_volume():  
    speak("Muting volume")  
    pyautogui.press("volumemute")