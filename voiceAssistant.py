import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if (hour >= 0 and hour < 12):
        speak('Good Morning')
    elif (hour >= 12 and hour < 18):
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('I am Jarvis Master Ehmad, Please tell me how I may help you.')


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-us')
            print(f'User Said: {query}')

        except Exception:
            print('Say that again please.')
            query = takeCommand().lower()
            return query
        return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'your name' in query:
            speak('I am Jarvis')
        elif 'who are you' in query:
            speak('I am Jarvis, working for Ehmad')
        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir the time is {strTime}')
        elif 'open code' in query:
            codePath = "C:\\Users\\Ehmad Saeed\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)