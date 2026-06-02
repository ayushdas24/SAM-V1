
from ddgs import DDGS  
import pywhatkit  
from modules.voice import speak  

def search_web(query, should_speak=True):  
    try:  
        query = query.replace("search for", "").replace("look up", "").strip()  
        if query:  
            if should_speak:
                speak(f"searching the web for {query}")  

            with DDGS() as ddgs:  
                results = list(ddgs.text(query, max_results=2))  

                if results:  
                    answer = results[0]["body"]  
                    print("Results:", answer)  

                    if should_speak:
                       speak(answer)  

                    return answer
                
                else:  
                    msg = "Sorry I couldn't find anything on that" 

                    if should_speak:
                       speak(msg)

                    return msg
                    
    except Exception as e:    
        print("search error:", e)     
        msg = f"search failed: {e}"

        if should_speak:
           speak("Something went wrong while searching.")  

           return msg

def youtube_play(query, should_speak=True):  
    video = query.replace("play", "").strip()

    if should_speak:
        speak("playing on youtube")

    pywhatkit.playonyt(video)
    return f"playing '{video}' on youtube"  

def google_search(query, should_speak=True):  

    if should_speak:
       speak("searching in google")  

    pywhatkit.search(query)
    return f"Google search opened for {query}"