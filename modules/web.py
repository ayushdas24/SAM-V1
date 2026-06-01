
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

                    return answer
                
                else:  
                    msg = "Sorry I couldn't find anything on that" 
                    speak(msg)
                    return msg
                    
    except Exception as e:    
        print("search error:", e)     

        msg = f"search failed: {e}"
        speak("Something went wrong while searching.")  
        return msg

def youtube_play(query):  
    speak("playing on youtube")  

    video = query.replace("play", "").strip()

    pywhatkit.playonyt(video)
    return f"playing '{video}' on youtube"  

def google_search(query):  
    speak("searching in google")  
    pywhatkit.search(query)

    return f"Google search opened for {query}"