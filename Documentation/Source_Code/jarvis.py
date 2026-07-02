import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(command)
        return command.lower()
    except:
        return ""

wish()

while True:
    command = take_command()

    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        webbrowser.open("https://www.google.com")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(current_time)

    elif "exit" in command:
        speak("Goodbye")
        break
