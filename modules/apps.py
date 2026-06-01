import os  
from modules.voice import speak  
from modules.config import VSCODE_PATH, YOUTUBE_URL

app_commands = {  
    "open notepad": lambda: os.startfile("notepad.exe"),  
    "open calculator": lambda: os.startfile("calc.exe"),  
    "open chrome": lambda: os.startfile("chrome.exe"),  
    "open vscode": lambda: os.startfile(VSCODE_PATH),  
    "open vs code": lambda: os.startfile(VSCODE_PATH),
    "open youtube": lambda: os.startfile(YOUTUBE_URL)
}  

def handle_apps(command):  
    for app in app_commands:  
        if app in command:  
            try:  
                speak(f"Opening {app.replace('open ', '')}")  
                app_commands[app]()  
            except Exception:  
                speak(f"Sorry, {app.replace('open ', '')} could not be opened.")  
            return True  
    return False

def launch_app(app_name: str):
    app_name = app_name.lower().strip()

    app_map = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "chrome.exe",
        "vscode": VSCODE_PATH,
        "vs code": VSCODE_PATH,
        "youtube":  YOUTUBE_URL
     
     }

    if app_name not in app_map:
        return f"Application '{app_name}' not found."
    
    try:
            speak(f"opening {app_name}")
            os.startfile(app_map[app_name])
            return f"{app_name} launched successfully."
    except Exception as e:
            print(f"launch error: {e}")
            speak(f"sorry, {app_name} could not be opened.")
            return f"failed to launch {app_name}: {e}"