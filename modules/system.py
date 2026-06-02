import os  
import ctypes  
import psutil  
import pyautogui  
from modules.voice import speak  

def shutdown(should_speak=True):  
    msg = "Shutting down the system in 10 seconds please save the work"
    if should_speak:
        speak(msg)
    os.system("shutdown /s /t 10")  

    return msg

def restart(should_speak=True):  
    msg = "Restarting the system in 10 seconds please save the work"
    if should_speak:
        speak(msg)
    os.system("shutdown /r /t 10")  

    return msg

def lock_system(should_speak=True):
  msg = "Locking your system"
  if should_speak:
    speak(msg)
    ctypes.windll.user32.LockWorkStation()  

    return msg

def system_status(should_speak=True):  
    battery = psutil.sensors_battery()  

    if battery:  
        percent = battery.percent  
        charging = "charging" if battery.power_plugged else "not charging"  
        status = f"Battery is at {percent}% and is currently {charging}"
        print(f"[system] {status}")

        if should_speak:
           speak(status)

        return status
     
    else:

        msg= "Sorry, I couldn't fetch battery information."  
        print(f"[system] {msg}")

        if should_speak:
         speak(msg)

        return msg

def volume_up(should_speak=True):  
    msg = "Increasing volume"
    if should_speak:
        speak(msg)

    for _ in range(5):  
        pyautogui.press("volumeup")

    return "system volume increased"  

def volume_down(should_speak=True):  
    msg = "Decreasing volume"
    if should_speak:
        speak(msg)

    for _ in range(5):  
        pyautogui.press("volumedown")  

    return "system volume decreased"

def mute_volume(should_speak=True):  
    msg = "Muting volume"
    if should_speak:
        speak(msg)
    pyautogui.press("volumemute")
    
    return "system volume muted"