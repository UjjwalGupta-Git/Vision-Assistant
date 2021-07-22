import speech_recognition as sr
import pyttsx3
import requests
import json

# Recognizer object
r = sr.Recognizer()

# Function to convert text to speech
def Speak(command, speed):
    engine = pyttsx3.init()

    # changes the speed of voice
    engine.setProperty('rate', speed)

    engine.say(command) 
    engine.runAndWait()

# Function to tell a joke
def TellAJoke():
    randomJokeUrl = "https://official-joke-api.appspot.com/random_joke"
    jokeJSONData = requests.get(randomJokeUrl).json()
    setup = jokeJSONData["setup"]
    punchLine = jokeJSONData["punchline"]
    Speak(setup, 150)
    Speak(punchLine, 150)

TellAJoke()

while(True):
    with sr.Microphone() as source:

        print("calibrating for ambient noise")

        # Adjusts for ambient noise
        r.adjust_for_ambient_noise(source, duration=1)

        print("listening...")

        # Collects AudioData and stores it in audio variable
        audio = r.listen(source, timeout=5)

        # converts AudioData into text
        text = r.recognize_google(audio, language='en-US')

