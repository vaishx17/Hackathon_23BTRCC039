from modules.speech import speak

def control_lights(state):
    if state == "on":
        speak("Turning on the lights.")
    elif state == "off":
        speak("Turning off the lights.")

def set_temperature(temp):
    speak(f"Setting temperature to {temp} degrees Celsius.")
