import os
import pyautogui
import screen_brightness_control as sbc
from modules.speech import speak

def shutdown():
    """Shuts down the computer."""
    speak("Shutting down the system in 5 seconds.")
    os.system("shutdown /s /t 5")  # Windows
    # os.system("sudo shutdown -h now")  # Uncomment for Linux/macOS

def restart():
    """Restarts the computer."""
    speak("Restarting the system in 5 seconds.")
    os.system("shutdown /r /t 5")  # Windows
    # os.system("sudo shutdown -r now")  # Uncomment for Linux/macOS

def lock_screen():
    """Locks the computer screen."""
    speak("Locking the screen.")
    os.system("rundll32.exe user32.dll,LockWorkStation")  # Windows only

def increase_volume():
    """Increases volume by 5 steps."""
    speak("Increasing volume.")
    for _ in range(5):
        pyautogui.press("volumeup")

def decrease_volume():
    """Decreases volume by 5 steps."""
    speak("Decreasing volume.")
    for _ in range(5):
        pyautogui.press("volumedown")

def mute_audio():
    print("DEBUG: Inside mute_audio()")  # Check if this runs
    """Mutes the system volume."""
    speak("Muting volume.")
    pyautogui.press("volumemute")

def unmute_audio():
    """Unmutes the system volume."""
    speak("Unmuting volume.")
    pyautogui.press("volumemute")  # Pressing again unmutes

def increase_brightness():
    """Increases screen brightness by 10%."""
    try:
        current_brightness = sbc.get_brightness()
        new_brightness = min(current_brightness[0] + 10, 100)  # Max 100%
        sbc.set_brightness(new_brightness)
        speak(f"Increasing brightness to {new_brightness} percent.")
    except Exception:
        speak("Sorry, I couldn't adjust the brightness.")

def decrease_brightness():
    """Decreases screen brightness by 10%."""
    try:
        current_brightness = sbc.get_brightness()
        new_brightness = max(current_brightness[0] - 10, 0)  # Min 0%
        sbc.set_brightness(new_brightness)
        speak(f"Decreasing brightness to {new_brightness} percent.")
    except Exception:
        speak("Sorry, I couldn't adjust the brightness.")

def control_system(command):
    command = command.lower().strip()

    print(f"DEBUG: Raw command received -> {command}")  # Debugging

    if "increase" in command and "volume" in command:
        print("DEBUG: Increase volume detected")
        increase_volume()
    elif "decrease" in command and "volume" in command:
        print("DEBUG: Decrease volume detected")
        decrease_volume()
    elif "mute" in command:  # Fixing mute command detection
        print("DEBUG: Mute audio detected")  
        mute_audio()
    elif "unmute" in command or "unmute audio" in command:  # Fixing unmute detection
        print("DEBUG: Unmute audio detected")
        unmute_audio()
    elif "increase" in command and "brightness" in command:
        print("DEBUG: Increase brightness detected")
        increase_brightness()
    elif "decrease" in command and "brightness" in command:
        print("DEBUG: Decrease brightness detected")
        decrease_brightness()
    elif "shutdown" in command:
        print("DEBUG: Shutdown detected")
        shutdown()
    elif "restart" in command:
        print("DEBUG: Restart detected")
        restart()
    elif "lock screen" in command:
        print("DEBUG: Lock screen detected")
        lock_screen()
    else:
        print("DEBUG: Command not recognized.")
        speak("I can't perform that system command.")

    print(f"DEBUG: Finished processing command -> {command}")
