import os
import sys
from dotenv import load_dotenv
from modules import voice, router, brain

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "")

if not API_KEY or API_KEY == "your_api_key_here":
    voice.speak("Warning. Gemini API Key is missing. Please check your dot env file.")
    print("[WARNING] GEMINI_API_KEY not found in .env. Brain module disabled.")
    # We could exit, but maybe they just want local commands
    SAM_V1_BRAIN = None
else:
    SAM_V1_BRAIN = brain.SAMGenerativeBrain(api_key=API_KEY)

# Initial Greeting
voice.speak("All systems online, sir.")  

while True:  
    # 1. Passive Listening Phase
    print("\n[Passive] Waiting for wake word 'sam'...")
    awake = voice.listen_for_wake_word("sam")
    
    if not awake:
        continue
    
    # 2. Active Command Phase
    voice.speak("Yes Sir?")
    command = voice.listen_for_command()
    
    if command is None: 
        continue

    command = command.lower().strip()
    print(f"DEBUG: You said -> {command}") 

    # EXIT
    if "exit" in command or "quit" in command:
        voice.speak("Systems offline.")
        sys.exit()

    # ROUTE LOCAL COMMANDS
    handled_locally = router.route_command(command)

    # BRAIN (If nothing else matched)
    if not handled_locally:
        if SAM_V1_BRAIN and len(command) > 1: # Make sure it's not just a random noise
            print("!!! TRIGGERED: BRAIN !!!")
            ai_reply = SAM_V1_BRAIN.think(command)
            print(f"SAM: {ai_reply}")
            voice.speak(ai_reply)
        elif not SAM_V1_BRAIN:
            voice.speak("I cannot process that command locally, and my neural link is offline.")