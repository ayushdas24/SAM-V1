
from duckduckgo_search import DDGS  
import pywhatkit  
from modules.voice import speak  

def search_web(query):  
    try:  
        query = query.replace("search for", "").replace("look up", "").strip()  
        if query:  
            speak(f"searching the web for {query}")  
            with DDGS() as ddgs:  
                results = list(ddgs.text(query, max_results=2))  
                if results:  
                    answer = results[0]["body"]  
                    print("Results:", answer)  
                    speak(answer)  
                else:  
                    speak("sorry, I couldn't find anything on that.")  
    except Exception as e:    
        print("search error:", e)     
        speak("Something went wrong while searching.")  

def youtube_play(query):  
    speak("playing on youtube")  
    pywhatkit.playonyt(query.replace("play", "").strip())  

def google_search(query):  
    speak("searching in google")  
    pywhatkit.search(query)