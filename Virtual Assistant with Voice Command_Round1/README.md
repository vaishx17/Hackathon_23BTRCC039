# Hackathon_23BTRCC039
# Virtual Assistant with Voice Command
**Overview**
This **Virtual Assistant** is a **Python-based AI assistant** that can perform various system-level tasks using voice commands. It can open and close applications, control system settings, perform web searches, and more.

## **Features**
- ✅ **Wake Word Activation** - Listens for "Hey Assistant" to activate.  
- ✅ **Open & Close Applications** - Open **any installed application** (Notepad, Word, Chrome, etc.).  
- ✅ **Control System Settings** - Increase/decrease **volume**, shutdown, restart, take screenshots, and manage files.  
- ✅ **Perform Web Searches** - Get instant search results from the web.  
- ✅ **Fetch Weather Updates** - Retrieve current weather conditions.  
- ✅ **Play Music** - Play songs from **Spotify or YouTube** (To be added).  
- ✅ **Log Opened Apps** - Keeps track of applications that were opened.  
- ✅ **Modular Architecture** - Organized helper modules for better scalability.  
---
## **Folder Structure**
VirtualAssistant/
│── laptop_assistant.py      # Main script for the assistant
│── wake_word.py             # Listens for the wake word ("Hey Assistant")
│── server.py                # Handles internal communication
│── opened_apps.log          # Logs opened applications
│── requirements.txt         # Dependencies
│── README.md                # Documentation
│── modules/                 # Organized helper modules
│   ├── speech.py           # Handles speech recognition & TTS
│   ├── system_control.py   # Controls system settings
│   ├── app_launcher.py     # Opens and closes applications
│   ├── web_search.py       # Performs web searches
---
## **Setup Instructions**

### **Prerequisites**
- **Python 3.x** installed on your system.  
- Required libraries listed in `requirements.txt`.  

### **Install Dependencies**
Run the following command to install required libraries:  
```bash
pip install -r requirements.txt
---
Run the Virtual Assistant
1.To the server ,run:
python server.py
2.To start the assistant, run:
python wake_word.py
---
Voice Command Examples

Application Control

"Open Chrome" - Opens Google Chrome.

"Close Notepad" - Closes Notepad.


System Control

"Increase volume" - Increases the system volume.

"Take a screenshot" - Captures the screen.


Web & Info Retrieval

"Search for Python tutorials" - Performs a web search.

"What’s the weather today?" - Fetches current weather.



---

Future Improvements

🔹 Enhance natural language understanding (NLP).

🔹 Add more integrations (calendar, email, notifications).

🔹 Improve response time for commands.

🔹 Implement Spotify/YouTube music playback.







