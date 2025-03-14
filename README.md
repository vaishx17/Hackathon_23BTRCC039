# Hackathon_23BTRCC039
# Virtual Assistant with Voice Commands

 Overview
This Virtual Assistant is a Python-based AI assistant that can perform various system-level tasks on your laptop using voice commands. It can open applications, perform web searches, and control smart home devices.

 Features
- Open any installed application (e.g., Notepad, Word, Chrome, etc.)
- Control system settings (adjust volume, shutdown, restart)
- Perform web searches
- Fetch weather updates
- Play music from Spotify or YouTube**
- Smart Home Contro (Turn on/off lights, control smart appliances)

Folder Structure

VirtualAssistant/
│── laptop_assistant.py        # Main script for the assistant
│── requirements.txt           # Dependencies
│── README.md                  # Documentation
│── modules/                   # Organized helper modules
│   ├── speech.py              # Handles speech recognition & TTS
│   ├── system_control.py      # Controls system settings
│   ├── app_launcher.py        # Opens applications
│   ├── web_search.py          # Performs web searches
│   ├── smart_home.py          # Manages smart home control
`

Setup Instructions
 Prerequisites
Ensure you have Python 3.x installed on your system.

Install Dependencies
Run the following command to install required libraries:

pip install -r requirements.txt


 Run the Virtual Assistant
To start the assistant, run:

python laptop_assistant.py


Voice Commands Examples

"Open Notepad"                - Opens Notepad application 
 "Search for Python tutorials"- Performs a web search on the topic 
 "What’s the weather today?"   - Fetches current weather updates 
 "Turn off the lights"         - Controls smart home devices 

Future Improvements
Enhance natural language understanding
Improve response time
Add more integrations (calendar, emails, etc.)



