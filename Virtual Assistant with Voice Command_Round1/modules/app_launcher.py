import os
import subprocess
import pygetwindow as gw
import difflib
from modules.speech import speak

# Dictionary for manually defined application paths
CUSTOM_APP_PATHS = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "command prompt": "cmd.exe",
    "file explorer": "explorer.exe",
    "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    "visual studio code": "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
}

# UWP (Microsoft Store) apps launch commands
UWP_APPS = {
    "calculator": "ms-calculator:",
    "mail": "outlookmail:",
    "store": "ms-windows-store:",
    "camera": "microsoft.windows.camera:",
}

def log_app_opening(app_name):
    """Logs opened applications."""
    with open("opened_apps.log", "a") as log_file:
        log_file.write(f"{app_name}\n")

def find_best_match(user_input, choices):
    """Finds the closest app match using fuzzy matching."""
    match = difflib.get_close_matches(user_input, choices, n=1, cutoff=0.6)  # 60% similarity
    return match[0] if match else None

def get_application_path(app_name):
    """Finds the correct path to an installed application."""
    
    # Check if app is in predefined paths
    if app_name in CUSTOM_APP_PATHS:
        return CUSTOM_APP_PATHS[app_name]
    
    # Check if app is a UWP app
    if app_name in UWP_APPS:
        return UWP_APPS[app_name]

    # Check PATH environment for system-installed apps
    try:
        result = subprocess.run(["where", app_name], capture_output=True, text=True, shell=True)
        if result.stdout:
            return result.stdout.split("\n")[0].strip()
    except Exception:
        pass

    # Search common directories
    common_paths = [
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        "C:\\Windows\\System32"
    ]

    for path in common_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().startswith(app_name.lower()) and file.endswith(".exe"):
                    return os.path.join(root, file)

    return None  # If not found

def open_app(app_name):
    """Opens an application based on user input."""
    app_name = app_name.lower().strip()
    
    app_path = get_application_path(app_name)
    if not app_path:
        # Try finding a close match
        best_match = find_best_match(app_name, CUSTOM_APP_PATHS.keys())
        if best_match:
            speak(f"Did you mean {best_match}? Opening now.")
            app_path = CUSTOM_APP_PATHS[best_match]
        else:
            speak(f"Sorry, I couldn't find {app_name} installed.")
            return
    
    try:
        if app_path.startswith("ms-"):  # Handle UWP Apps
            subprocess.run(["powershell", "Start-Process", app_path], shell=True)
        else:
            subprocess.Popen(app_path, shell=True)
        
        log_app_opening(app_name)  # Log the app opening
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Error opening {app_name}: {e}")
        print(f"Error: {e}")

def get_matching_window(app_name):
    """Finds a window matching the app name."""
    windows = gw.getAllTitles()
    for title in windows:
        if app_name.lower() in title.lower():
            return gw.getWindowsWithTitle(title)[0]
    return None

def minimize_app(app_name):
    """Minimizes an open application."""
    window = get_matching_window(app_name)
    if window:
        window.minimize()
        speak(f"Minimized {app_name}")
    else:
        speak(f"Could not find an open window for {app_name}")

def maximize_app(app_name):
    """Maximizes an open application."""
    window = get_matching_window(app_name)
    if window:
        window.maximize()
        speak(f"Maximized {app_name}")
    else:
        speak(f"Could not find an open window for {app_name}")

def close_app(app_name):
    """Closes an open application."""
    window = get_matching_window(app_name)
    if window:
        window.close()
        speak(f"Closed {app_name}")
    else:
        speak(f"Could not find an open window for {app_name}")
