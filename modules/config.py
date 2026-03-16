
import queue  
import pyttsx3  

# Initialize the TTS engine
engine = pyttsx3.init()  

# Set speech rate (words per minute)
engine.setProperty('rate', 160)  

# Set speech volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)  

# Queue for non-blocking speech execution
speak_queue = queue.Queue()