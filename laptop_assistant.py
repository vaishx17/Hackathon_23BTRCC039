import sys
import webbrowser
import requests
import json
from modules.speech import recognize_speech, speak
from modules.app_launcher import open_app, close_app, minimize_app, maximize_app, find_best_match
from modules.system_control import control_system
from modules.web_search import search_google, play_music, get_weather
from modules.smart_home import control_lights, set_temperature  # Import smart home functions

def send_notification(title, message):
    url = "http://127.0.0.1:5000/notify"
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"title": title, "message": message})

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print("Failed to send notification:", response.text)

def main():
    speak("Hello! I'm your virtual assistant. How can I help you?")
    
    while True:
        try:
            command = recognize_speech()
            if command:
                print(f"You said: {command}")

                # Smart Home Control
                if "turn on the lights" in command:
                    control_lights("on")
                elif "turn off the lights" in command:
                    control_lights("off")
                elif "set temperature to" in command:
                    try:
                        temp = int(command.split("set temperature to")[1].strip().split()[0])
                        set_temperature(temp)
                    except ValueError:
                        speak("Sorry, I couldn't understand the temperature value.")

                elif "open" in command:
                    app_name = command.replace("open", "").strip()
                    app_list = [
                        "notepad", "chrome", "word", "excel", "discord", "spotify", "file explorer", "calculator",
                        "vlc", "photoshop", "powerpoint", "cmd", "terminal", "paint", "edge", "onenote"
                    ]
                    best_match = find_best_match(app_name, app_list)
                    
                    if best_match:
                        open_app(best_match)
                        send_notification("App Opened", f"{best_match} has been opened.")  # Add this line
                    else:
                        speak(f"Sorry, I couldn't find {app_name}")

                elif "close" in command:
                    app_name = command.replace("close", "").strip()
                    close_app(app_name)
                    send_notification("App Closed", f"{app_name} has been closed.")  # Add this line

                elif "minimize" in command or "minimise" in command:
                    app_name = command.replace("minimize", "").replace("minimise", "").strip()
                    minimize_app(app_name)

                elif "maximize" in command:
                    app_name = command.replace("maximize", "").strip()
                    maximize_app(app_name)

                elif any(keyword in command for keyword in [
                    "increase volume", "decrease volume", "mute audio", "unmute audio", 
                    "shutdown", "restart", "lock screen", "increase brightness", "decrease brightness"
                ]):
                    print(f"DEBUG: Sending to control_system -> {command}")
                    control_system(command)
                    send_notification("System Command", f"Executed: {command}")  # Add this line

                elif "search for" in command:
                    query = command.replace("search for", "").strip()
                    search_google(query)

                elif "play" in command and "on YouTube" in command:
                    play_music(command)

                elif "what's the weather" in command or "weather update" in command:
                    get_weather()

                elif "exit" in command or "quit" in command:
                    send_notification("Assistant Stopped", "The virtual assistant has been closed.")  # Add this line
                    speak("Goodbye!")
                    sys.exit()

                else:
                    speak("Sorry, I didn't understand that.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
