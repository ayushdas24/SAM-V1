import os  
from modules.voice import speak  

app_commands = {  
    "open notepad": lambda: os.startfile("notepad.exe"),  
    "open calculator": lambda: os.startfile("calc.exe"),  
    "open chrome": lambda: os.startfile("chrome.exe"),  
    "open vscode": lambda: os.startfile(r"D:\Microsoft VS Code\Code.exe")  
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