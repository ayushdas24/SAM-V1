# 🧠 SAM-V1 — System Automation Module

> [!IMPORTANT]
> **Archived:** SAM-V1 is frozen and no longer under active development.
> It is preserved as the original proof of concept and as a reference for SAM-V2.
> No new features, refactors, or maintenance fixes are planned for this version.

> **"All systems online, sir. How may I assist?"**

SAM-V1 is a voice-controlled AI assistant built in Python that combines local system automation, voice interaction, and Generative AI capabilities into a single modular framework.

Originally developed as the foundation of the **DedSec AI Ecosystem**, SAM-V1 focuses on creating a practical desktop assistant capable of understanding voice commands, performing local automation tasks, and interacting with Large Language Models.

---

## 🚀 Current Status

**SAM-V1 Core Stable ✅**

### Working Features

* Wake Word Detection ("Sam")
* Speech-to-Text Command Processing
* Text-to-Speech Responses
* Application Launcher
* Date & Time Utilities
* Battery Status Monitoring
* Screenshot Capture
* Web Search Integration
* YouTube Playback
* Flask + SocketIO Dashboard
* Gemini AI Integration

### Under Development

* Persistent Memory
* Task Planning Engine
* Agentic Workflows
* Multi-Agent Coordination
* Advanced System Automation

---

## 🧠 Generative AI Core

SAM-V1 integrates Google's Gemini model to provide conversational reasoning beyond predefined commands.

### Capabilities

* Natural Language Understanding
* Context-Aware Responses
* Dynamic Tool Invocation
* Fallback Reasoning when local commands are unavailable

---

## 🛠 Features

| Category          | Capabilities                                       |
| ----------------- | -------------------------------------------------- |
| Voice Interface   | Wake Word Detection, STT, TTS                      |
| Local Automation  | App Launching, System Controls                     |
| Utilities         | Date, Time, Jokes, Screenshots                     |
| System Operations | Battery Monitoring, Lock System                    |
| Web Operations    | DuckDuckGo Search, Google Search, YouTube Playback |
| Dashboard         | Live Status Monitoring via Flask & SocketIO        |
| AI Layer          | Gemini-Powered Conversational Intelligence         |

---

## 📂 Project Structure

```text
SAM-V1/
│
├── main.py                 # Core Runtime
├── server.py               # Web Dashboard Server
├── requirements.txt
│
├── modules/
│   ├── brain.py            # Gemini Integration
│   ├── voice.py            # Speech Recognition & TTS
│   ├── router.py           # Local Command Router
│   ├── agent_tools.py      # Function Calling Tools
│   ├── apps.py             # Application Launcher
│   ├── system.py           # System Controls
│   ├── web.py              # Web Operations
│   └── fun.py              # Utility Functions
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── app.js
│
└── .env
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/ayushdas24/SAM-V1.git
cd SAM-V1
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running SAM

### Terminal Mode

```bash
python main.py
```

### Dashboard Mode

```bash
python server.py
```

Open:

```text
http://localhost:5000
```

---

## 🏴 Future Roadmap

### Phase 2

* Enhanced Dashboard UI
* Persistent Conversation Memory
* Better Tool Routing
* Local Knowledge Storage

### Phase 3

* Autonomous Planning
* Multi-Step Task Execution
* Agentic Reasoning

### Phase 4

* DedSec Security Modules
* Cybersecurity Automation
* Advanced Reconnaissance Workflows

---

## 👨‍💻 Author

**Ayush Das**

AI Developer • Automation Builder • Cybersecurity Enthusiast

GitHub: https://github.com/ayushdas24

---

## ⚠️ Disclaimer

SAM-V1 is an educational and development project. Certain system-level actions can modify or control the host machine. Use responsibly.

---

> **"The first version isn't the destination. It's proof the idea works."**
