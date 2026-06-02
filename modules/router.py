from modules import system, fun, web, apps

COMMAND_MAP = [
    ("volume up",       lambda _: system.volume_up()),
    ("volume down",     lambda _: system.volume_down()),
    ("mute",            lambda _: system.mute_volume()),
    ("shutdown",        lambda _: system.shutdown()),
    ("restart",         lambda _: system.restart()),
    ("battery",         lambda _: system.system_status(should_speak=True)),
    ("status",          lambda _: system.system_status(should_speak=True)),
    ("lock",            lambda _: system.lock_system()),
    ("screenshot",      lambda _: fun.take_screenshot()),
    ("what time",       lambda _: fun.tell_time()),
    ("what's the time", lambda _: fun.tell_time()),
    ("time",            lambda _: fun.tell_time()),
    ("what date",       lambda _: fun.tell_date()),
    ("date",            lambda _: fun.tell_date()),
    ("tell me a joke",  lambda _: fun.tell_jokes()),
    ("joke",            lambda _: fun.tell_jokes()),
    ("play",            lambda cmd: web.youtube_play(cmd)),
    ("search for",      lambda cmd: web.search_web(cmd)),
    ("look up",         lambda cmd: web.search_web(cmd)),
    ("search",          lambda cmd: web.search_web(cmd)),
    ("google",          lambda cmd: web.google_search(cmd.replace("google", "").strip())),
]

LOCAL_KEYWORDS = [
    "volume up", "volume down", "mute", "shutdown", "restart", "battery", "status",
    "lock", "screenshot", "what time", "what's the time", "time",
    "what date", "date", "tell me a joke", "joke",
    "play", "search for", "look up", "search", "google"
]

def route_command(command: str) -> bool:
    """
    Called by main.py for every spoken command.
    Checks command against COMMAND_MAP triggers.
    Returns True if handled locally, False if Gemini should handle it.
    """
    if apps.handle_apps(command):
        return True

    for trigger, action in COMMAND_MAP:
        if trigger in command:
            print(f"[Router] Match trigger: {trigger}")
            action(command)
            return True
        
    if any(word in command for word in LOCAL_KEYWORDS):
        print("[Router] Command contains local keyword but no trigger matched.")
        return True

    return False