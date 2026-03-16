SAM-V1 — The Origin of DedSec
"All systems online, sir. How may I assist?"
SAM (System Automation Module) is a hybrid voice assistant that merges local system automation with a Generative AI brain.
This is Version 1 — the foundation of a future autonomous AI ecosystem called DedSec.
SAM-V1 combines voice interaction, system control, and generative intelligence to create a modular AI assistant capable of understanding commands, performing OS operations, and responding conversationally.
🧠 Generative Core
Unlike traditional rule-based assistants, SAM-V1 is powered by the Gemini 1.5 Flash model from Google.
This enables:
Contextual Conversations
SAM understands intent, not just fixed commands.
DedSec Persona
A built-in system prompt maintains a loyal, witty, hacker-style personality throughout interactions.
Dynamic Problem Solving
If a local command cannot be executed, the generative brain takes over to provide answers or assistance.
🛠 Features
Neural Link (Generative AI)
Real-time reasoning and response generation using a generative model.
Voice Interface
Speech recognition and threaded text-to-speech for smooth conversation.
OS Integration
System level controls including:
system lock
volume control
screenshot capture
System Awareness
Live system data such as:
battery status
charging state
Web Operations
DuckDuckGo search queries
YouTube video playback
Utilities
application launching (Notepad, Calculator, etc.)
jokes and small interactions
time and date queries
📂 Project Structure

SAM-V1
│
├── main.py            # Main execution loop
│
├── modules
│   ├── brain.py       # Gemini AI integration
│   ├── voice.py       # Speech recognition & TTS engine
│   ├── apps.py        # Application launcher
│   ├── system.py      # OS & hardware control
│   ├── web.py         # Web and YouTube search
│   └── fun.py         # Utility and entertainment features
The architecture follows a modular design, allowing components to evolve independently as the system grows.
🚀 Evolution: From Assistant to Agent
SAM-V1 represents the first stage of a larger vision.
The system is evolving into DedSec, an agent-driven AI ecosystem designed for:
autonomous decision making
modular intelligence systems
advanced cybersecurity operations
distributed AI orchestration
SAM is the foundation layer of that architecture.
🛠 Setup
1. Clone the repository

git clone https://github.com/ayushdas24/SAM-V1.git
cd SAM-V1
2. Install dependencies

pip install pyttsx3 speechrecognition google-generativeai psutil pyautogui
3. Add your Gemini API key
Insert your API key inside main.py.
4. Run SAM

python main.py
👤 Author
Ayush Das
AI Developer & Penetration Tester
🏴 DedSec
Join the network.
We Are Many. We Are DedSec.
