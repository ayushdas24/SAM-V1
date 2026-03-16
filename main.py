from modules import voice, apps, system, web, fun, brain
import sys

# Initial Greeting
voice.speak("All systems online, sir.")  

SAM_V1_BRAIN = brain.SAMGenerativeBrain(api_key="AIzaSyBP4gcDVA8kESwXAEgh0l_t_FBl44pJG6I")

while True:  
    command = voice.listen(timeout=15)
    
    if command is None: 
        continue

    command = command.lower().strip()
    print(f"DEBUG: You said -> {command}") 

    # 1. EXIT
    if "exit" in command or "quit" in command:
        voice.speak("Systems offline.")
        sys.exit()

    # 2. SYSTEM CONTROLS
    elif "battery" in command or "status" in command:
        print("!!! TRIGGERED: BATTERY !!!")
        system.system_status()
    
    elif "lock" in command:
        print("!!! TRIGGERED: LOCK !!!")
        system.lock_system()

    elif "volume up" in command:
        print("!!! TRIGGERED: VOL UP !!!")
        system.volume_up()

    elif "volume down" in command:
        print("!!! TRIGGERED: VOL DOWN !!!")
        system.volume_down()

    # 3. FUN & INFO
    elif "joke" in command:
        print("!!! TRIGGERED: JOKE !!!")
        fun.tell_jokes()

    elif "time" in command:
        print("!!! TRIGGERED: TIME !!!")
        fun.tell_time()

    elif "date" in command:
        print("!!! TRIGGERED: DATE !!!")
        fun.tell_date()

    elif "screenshot" in command:
        print("!!! TRIGGERED: SCREENSHOT !!!")
        fun.take_screenshot()

    # 4. WEB & APPS
    elif "play" in command:
        print("!!! TRIGGERED: PLAY !!!")
        web.youtube_play(command)

    elif "search" in command:
        print("!!! TRIGGERED: SEARCH !!!")
        web.search_web(command)

    # 5. BRAIN (If nothing else matched)
    else:
        if len(command) > 1: # Make sure it's not just a random noise
            print("!!! TRIGGERED: BRAIN !!!")
            ai_reply = SAM_V1_BRAIN.think(command)
            print(f"SAM: {ai_reply}")
            voice.speak(ai_reply)