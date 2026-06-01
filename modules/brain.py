import google.generativeai as genai
from modules.agent_tools import TOOLS_LIST

class SAMGenerativeBrain:
    def __init__(self, api_key):
        # Initialise the LLM Arsenal
        genai.configure(api_key=api_key)
        
        # The soul of SAM (System Instructions)
        self.identity = (
            "You are SAM, an autonomous AI Agent built by Lewis (Ayush Das). "
            "You operate as a highly intelligent, precise, and witty DedSec operative. "
            "You have direct programmatic access to the host's Windows computer through your provided Tools. "
            "If the user asks you to perform an action available in your tools, call the tool autonomously. "
            "If they ask you a conversational question, answer directly with zero fluff. "
            "WARNING: Do not execute sys_shutdown or sys_restart unless the user explicitly commands it."
        )
        
        # Inject the Tool Payload and System Identity into the Core
        self.model = genai.GenerativeModel(
            model_name='gemini-2.0-flash',
            tools=TOOLS_LIST,
            system_instruction=self.identity
        )
        
        # Initialize the Stateful Neural Link with Auto-Execution active
        self.chat = self.model.start_chat(
            history=[], 
            enable_automatic_function_calling=True
        )

    def think(self, user_input):
        try:
            response = self.chat.send_message(user_input)
            return response.text
        
        except Exception as e:
            error_text = str(e)
            print(f"Brain Error: {e}")

            if "429" in error_text or "Quota exceeded" in error_text:
             return "Gemini quota is exhausted right now, sir. Local commands are still online."
    
            return "My neural link is flickering, sir. Encountered an execution error in the tool pipeline."