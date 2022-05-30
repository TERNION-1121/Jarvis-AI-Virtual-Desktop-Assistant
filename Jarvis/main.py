import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib

MASTER = "ternion"

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


# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...\n")
        query = r.recognize_google(audio, language = 'en - in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please")
        speak("Say that again please")
        query = None
    return query.lower()


# This function will send an email
# It is not recommended to use this function, until you're willing to provide access to your email account, 
# To use this funcionality, please refer to https://support.google.com/accounts/answer/6010255?hl=en beforehand
''' 
def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your@email.com', 'your_password')
    server.sendmail("your@email.com", to, content)
    server.close() 
'''

# Main Program starts here...

def main():
    print("Initializing Jarvis...")
    speak("Initializing Jarvis...")
    wishMe()
    print("I am Jarvis. How can I help you?\n")
    speak("I am Jarvis. How can I help you?")
    
    query = takeCommand()

    # Logic for executing tasks as per the query 
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)

        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")


    elif 'open google' in query:
        webbrowser.open("https://www.google.com")

    elif 'open spotify' in query:
        webbrowser.open("https://open.spotify.com/")

    elif 'open reddit' in query:
        webbrowser.open("https://www.reddit.com")

    elif 'play music' in query:
        songs_dir = "E:\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\iBall\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    # elif logic to use the send email functionality
    '''
    elif 'email to' in query.lower():
        try:
            speak("What should I send?")
            content = takeCommand()
            to = "to_person@email.com"
            sendEmail(to, content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)
    '''

main()