import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib

MASTER = "ternion"

print("Initializing Jarvis")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function: Will pronounce the string which is passed to it as the arguement
def speak(text):
    engine.say(text)
    engine.runAndWait()


# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 6:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)

    speak("I am Jarvis. How may I help you?")


# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en - in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please")
        speak("Say that again please")

# Main Program starts here...

speak("Initializing Jarvis...")
wishMe()
takeCommand()