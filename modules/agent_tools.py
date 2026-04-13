"""
This module holds the strict Function Calling definitions for the SAM Autonomous Agent.
Gemini requires precise docstrings and type hints to understand HOW and WHEN to use these tools autonomously.
"""

from modules import system, fun, web, apps

def sys_volume_up() -> str:
    """Increases the computer system volume."""
    system.volume_up()
    return "Action Successful: System volume increased."

def sys_volume_down() -> str:
    """Decreases the computer system volume."""
    system.volume_down()
    return "Action Successful: System volume decreased."

def sys_mute() -> str:
    """Mutes the computer system speaker completely."""
    system.mute_volume()
    return "Action Successful: System volume muted."

def sys_lock() -> str:
    """Locks the windows user session."""
    system.lock_system()
    return "Action Successful: Administrator session secured and locked."

def sys_shutdown() -> str:
    """Initiates a complete bare-metal computer shutdown loop. Use with extreme caution."""
    system.shutdown()
    return "Action Successful: Initiated lethal system shutdown hook."

def sys_restart() -> str:
    """Initiates a computer reboot sequence. Use with extreme caution."""
    system.restart()
    return "Action Successful: Initiated system reboot sequence."

def sys_status() -> str:
    """Retrieves the current battery percentage and system health status."""
    system.system_status()
    return "Action Successful: Battery and system status executed." 

def util_get_time() -> str:
    """Retrieves the exact current local time."""
    fun.get_time()
    return "Action Successful: Time reported directly to user."

def util_get_date() -> str:
    """Retrieves the current local date."""
    fun.get_date()
    return "Action Successful: Date reported directly to user."

def util_take_screenshot() -> str:
    """Takes a graphical screen capture and writes the evidence to local disk."""
    fun.take_screenshot()
    return "Action Successful: Screenshot captured and saved to disk."

def search_wikipedia_duckduckgo(query: str) -> str:
    """Searches the internet / DuckDuckGo for general knowledge, data lookup, or wiki dumps."""
    web.search_web(query)
    return f"Action Successful: OSINT executed via DuckDuckGo for context '{query}'."

def search_google(query: str) -> str:
    """Forcibly opens a google search engine page in the user's web browser."""
    web.google_search(query)
    return f"Action Successful: Google search initiated in host browser for '{query}'."

def play_youtube(query: str) -> str:
    """Opens and plays a YouTube stream/video matching the given phrase."""
    web.youtube_play(query)
    return f"Action Successful: YouTube streaming initiated for '{query}'."

def launch_application(app_name: str) -> str:
    """Launches a desktop application by name natively (e.g. discord, notepad, chrome, vscode, terminal)."""
    apps.launch_app(app_name)
    return f"Action Successful: Requested execution payload for application: {app_name}."

# The Core Arsenal Payload mapped for GenAI Initialization
TOOLS_LIST = [
    sys_volume_up, sys_volume_down, sys_mute, sys_lock,
    sys_shutdown, sys_restart, sys_status,
    util_get_time, util_get_date, util_take_screenshot,
    search_wikipedia_duckduckgo, search_google, play_youtube, launch_application
]
