"""
This module holds the strict Function Calling definitions for the SAM Autonomous Agent.
Gemini requires precise docstrings and type hints to understand HOW and WHEN to use these tools autonomously.
"""

from modules import system, fun, web, apps

def sys_volume_up() -> str:
    """Increases the computer system volume."""
    return system.volume_up(should_speak=False)
    

def sys_volume_down() -> str:
    """Decreases the computer system volume."""
    return system.volume_down(should_speak=False)
    

def sys_mute() -> str:
    """Mutes the computer system speaker completely."""
    return system.mute_volume(should_speak=False)

def sys_lock() -> str:
    """Locks the windows user session."""
    return system.lock_system(should_speak=False)
   

def sys_shutdown() -> str:
    """Initiates a complete bare-metal computer shutdown loop. Use with extreme caution."""
    return system.shutdown(should_speak=False)

def sys_restart() -> str:
    """Initiates a computer reboot sequence. Use with extreme caution."""
    return system.restart(should_speak=False)
   

def sys_status() -> str:
    """Retrieves the current battery percentage and system health status."""
    return system.system_status(should_speak=False)
    
def util_get_time() -> str:
    """Retrieves the exact current local time."""
    return fun.get_time()
    

def util_get_date() -> str:
    """Retrieves the current local date."""
    return fun.get_date()

def util_take_screenshot() -> str:
    """Takes a graphical screen capture and writes the evidence to local disk."""
    return fun.take_screenshot(should_speak=False)
    
def search_wikipedia_duckduckgo(query: str) -> str:
    """Searches the internet / DuckDuckGo for general knowledge, data lookup, or wiki dumps."""
    return web.search_web(query, should_speak=False)
    

def search_google(query: str) -> str:
    """Forcibly opens a google search engine page in the user's web browser."""
    return web.google_search(query, should_speak=False)
   

def play_youtube(query: str) -> str:
    """Opens and plays a YouTube stream/video matching the given phrase."""
    return web.youtube_play(query, should_speak=False)
   

def launch_application(app_name: str) -> str:
    """Launches a desktop application by name natively (e.g. discord, notepad, chrome, vscode, terminal)."""
    return apps.launch_app(app_name, should_speak=False)
   
# The Core Arsenal Payload mapped for GenAI Initialization
TOOLS_LIST = [
    sys_volume_up, sys_volume_down, sys_mute, sys_lock,
    sys_shutdown, sys_restart, sys_status,
    util_get_time, util_get_date, util_take_screenshot,
    search_wikipedia_duckduckgo, search_google, play_youtube, launch_application
]
