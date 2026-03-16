from modules import voice, apps, system, web, fun  

dedsec = brain.DedSecBrain()

voice.speak("All systems online sir , how may i assists")

while True:
    command = voice.listen(timeout=15)

    if command is None:
        continue

    if "exit" in command or "quit" in command:
        voice.speak("Goodbye! stay safe sir")
        break

    #GET AGENTIC DECISION
    ai_response, active_engine = dedsec.query(command)
    print(f" [{active_engine}]: {ai_response}")

    #Agentic EXECUTION BRIDGE
    if "EXECUTE:" in ai_response:
        action = ai_response.replace("EXECUTE:", "").strip().lower()

        # Bridge the AI's decision to your existing modules
        if "open" in action: apps.handle_apps(action)
        elif "shutdown" in action: system.shutdown()
        elif "restart" in action: system.restart()
        elif "lock" in action: system.lock_system()
        elif "battery" in action or "status" in action: system.system_status()
        elif "volume up" in action: system.volume_up()
        elif "volume down" in action: system.volume_down()
        elif "mute" in action: system.mute_volume()
        elif "search for" in action: web.search_web(action)
        elif "play" in action: web.youtube_play(action)
        elif "screenshot" in action: fun.take_screenshot()
        elif "joke" in action: fun.tell_jokes()
        elif "time" in action: fun.tell_time()
        elif "date" in action: fun.tell_date()
    else:
        #If its not a command , SAM just speaks AI's response
        voice.speak(ai_response, wait=False)   