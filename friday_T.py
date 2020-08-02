#Friday tutorial

import pyttsx3
# import speech_recognition as sr 
import wikipedia
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour == 12:
        speak("Good Morning!")

    elif hour  >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

def writeCommand():
    # Takes written command
    query = input("\nWrite something...\n")
    return query


if __name__ == "__main__":
    
    wishMe()
    
    while True:
        query = writeCommand().lower()

        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            print("\nSearching Wikipedia...")
            speak("Searching Wikipedia...")
            print("According to Wikipedia\n")
            speak("According to Wikipedia")
            print("==>", results)
            speak(results)