from dataclasses import dataclass
from typing import Callable
from modules import system, fun, web, apps

@dataclass
class RouteResult:
    handled: bool
    source: str = "router"
    message: str = "" 
    error: str | None = None

def safe_execution(action: Callable, command: str, source :str) -> RouteResult:
    try:
        result = action(command)
        return RouteResult(
            handled=True,
            source=source,
            message=str(result) if result else "command executed successfully",
            error = None
        )
    except Exception as e:
        print(f"Router Error {source} command: {e}")
        return RouteResult(
            handled=True,
            source=source,
            message="command failed safely",
            error=str(e)
        )
    

COMMANDS = [
{
    "name": "Volume_up",
    "phrases": ["volume up", "increase volume", "turn up volume"],
    "action": lambda _: system.volume_up(),
},
{
    "name": "volume_down",
    "phrases": ["volume down", "decrease volume", "turn down volume"],
    "action": lambda _: system.volume_down(),
},
{
    "name": "mute",
    "phrases": ["mute", "unmute"],
    "action": lambda _: system.mute_volume(),
},
{
    "name": "battery_status",
    "phrases": ["battery status", "check battery", "battery level", "battery"],
    "action": lambda _: system.system_status(should_speak=True),
},
{
    "name": "lock_system",
    "phrases": ["lock","lock the system", "lock computer"],
    "action": lambda _: system.lock_system(),
},
{
    "name": "screenshot",
    "phrases": ["screenshot", "take screenshot"],
    "action": lambda _: fun.take_screenshot(),
},

{
    "name": "time",
    "phrases": ["what time", "what's the time", "what time is it", "current time", "tell time"],
    "action": lambda _: fun.tell_time(),
},
{
    "name": "date",
    "phrases": ["date", "what date", "today's date", "what is today's date"],
    "action": lambda _: fun.tell_date(),
},
{
    "name": "joke",
    "phrases": ["joke", "tell me a joke"],
    "action": lambda _: fun.tell_jokes(),
},
{
    "name": "youtube_play",
    "phrases": ["play"],
    "action": lambda cmd: web.youtube_play(cmd),
},
{
    "name": "web_search",
    "phrases": ["search for", "look up", "search"],
    "action": lambda cmd: web.search_web(cmd),
},
{
    "name": "google_search",
    "phrases": ["google"],
    "action": lambda cmd: web.google_search(cmd.replace("google", "").strip()),
},

]

LOCAL_KEYWORDS = [
    "volume", "mute", "battery", "status", "lock",
    "shutdown", "restart", "screenshot", "open",
    "play", "search", "google", "time", "date", "joke"
]

def match_phrase(command: str, phrases: list[str]) -> bool:
    command = command.lower().strip()

    for phrase in phrases:
        phrase = phrase.lower().strip()

        if command == phrase:
            return True
        
        if command.startswith(phrase + ""):
            return True
        
        if phrase in command:
            return True
        
    return False

def route(command: str) -> RouteResult:
    command = command.lower().strip()

    #app laucher first

    app_handle = apps.handle_apps(command)

    if app_handle:
        return RouteResult(
            handled=True,
            source="apps",
            message="Application command handled",
            error = None
        )
    

    # command registry

    for item in COMMANDS:
        if match_phrase(command, item["phrases"]):
            print(f"[Router] Match: {item['name']}")
            return safe_execution(item["action"], command, item["name"])
        

    #Local-like but unclear command should not waste gemini quota

    if any(word in command.split() for word in LOCAL_KEYWORDS):
        print(f"[Router] local-like command blocked from gemini fallback.")
        return RouteResult(
             handled=True,
             source="Router_guard",
             message="local command was unclear. please repeat more clearly.",
             error=None
        )
    
    return RouteResult(
        handled=False,
        source="Gemini_fallback",
        message="no local command to gemini",
        error=None
    )

def route_command(command: str) -> bool:
    """
    Backward-compatibility wrapper for main.py.
    Returns True if handled locally, False if gemini should handle it.
    """
    result = route(command)
    return result.handled