import speech_recognition as sr
import subprocess

def listen_for_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 'Hey Assistant'...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        wake_word = recognizer.recognize_google(audio).lower()
        print(f"You said: {wake_word}")

        if "hey assistant" in wake_word:
            print("Wake word detected! Activating assistant...")
            subprocess.run(["python", "laptop_assistant.py"])
        else:
            print("Wake word not detected. Try again.")

    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Speech recognition service error.")

if __name__ == "__main__":
    while True:
        listen_for_wake_word()
