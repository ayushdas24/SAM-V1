import google.generativeai as genai

class SAMGenerativeBrain:
    def __init__(self, api_key):
        #Initialise the LLM
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.chat = self.model.start_chat(history=[])

        #The soul of SAM-V1
        self.identity = (
            "You are SAM-V1, the first-generation AI created by Ayush. "
            "You are witty, loyal, and sound like a DedSec operative. "
            "Keep your answers concise and cool. If you can't do a task, "
            "just respond conversationally as a friend."
        )

    def think(self, user_input):
        try:
            #combine identity with user input for every thought
            prompt = f"{self.identity}\nUser: {user_input}"
            response = self.chat.send_message(prompt)
            return response.text
        except Exception as e:
            print(f"Brain Error: {e}")
            return "My neural link are flickering, sir.But i am still here."