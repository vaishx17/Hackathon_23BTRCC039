import webbrowser
from modules.speech import speak
import time

def search_google(query):
    """Searches Google for the given query."""
    speak(f"Searching Google for {query}.")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def play_music(command):
    """Plays music on YouTube based on command."""
    if "on YouTube" in command:
        song = command.replace("play", "").replace("on YouTube", "").strip()
        url = f"https://www.youtube.com/results?search_query={song}"
        webbrowser.open(url)

def get_weather():
    """Mock weather function (you can replace with actual API)."""
    try:
        print("DEBUG: Weather function is running.")
        speak("The current weather is sunny with 25 degrees Celsius.")  # Static response for now
    except Exception as e:
        print(f"Weather error: {e}")
