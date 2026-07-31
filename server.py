from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import os
import sys
import secrets
from dotenv import load_dotenv
from modules import voice, router
from modules.brain import gemini_brain

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SAM_SECRET_KEY")
socketio = SocketIO(app, async_mode='threading')

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "")

if not API_KEY or API_KEY == "your_api_key_here":
    print("[WARNING] GEMINI_API_KEY not found in .env. Brain module disabled.")
    SAM_V1_BRAIN = None
else:
    SAM_V1_BRAIN = gemini_brain.SAMGenerativeBrain(api_key=API_KEY)

def send_update(status, message=""):
    """Helper to emit websocket updates"""
    socketio.emit('sam_update', {'status': status, 'message': message})

def sam_loop():
    """Background thread running the original main.py logic"""
    voice.speak("Web server online, sir. Systems operational.")  
    
    while True:  
        send_update("IDLE", "Waiting for wake word 'sam'...")
        print("\n[Passive] Waiting for wake word 'sam'...")
        awake = voice.listen_for_wake_word("sam")
        
        if not awake:
            continue
        
        send_update("LISTENING", "Listening for command...")
        voice.speak("Yes Sir?")
        command = voice.listen_for_command()
        
        if command is None: 
            send_update("IDLE", "Command timeout")
            continue

        command = command.lower().strip()
        print(f"DEBUG: You said -> {command}") 
        send_update("PROCESSING", f"Command: {command}")

        # EXIT
        if "exit" in command or "quit" in command:
            send_update("OFFLINE", "Systems offline.")
            voice.speak_now("Systems offline.")
            os._exit(0)

        # ROUTING Local command first: Send raw command straight to the Agentic Function Crawler
        handled_locally = router.route_command(command)

        if handled_locally:
            send_update("RESPONDING", "Command executed locally")
            continue 

        if SAM_V1_BRAIN and len(command) > 1:
            print("!!! TRIGGERED: AUTONOMOUS BRAIN !!!")
            send_update("THINKING", "Consulting Payload Matrix...")
            ai_reply = SAM_V1_BRAIN.think(command)
            print(f"SAM: {ai_reply}")
            send_update("RESPONDING", ai_reply)
            voice.speak(ai_reply)

        elif not SAM_V1_BRAIN:
            send_update("ERROR", "Neural link offline.")
            voice.speak("My Neural link is down, sir. I cannot execute tools.")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Start SAM core loop in a background thread
    threading.Thread(target=sam_loop, daemon=True).start()
    print("Starting DedSec Web Interface on http://localhost:5000")
    socketio.run(app, debug=False, host='127.0.0.1', port=5000)
