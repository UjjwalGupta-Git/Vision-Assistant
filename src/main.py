import speech_recognition as sr
import pyttsx3
import requests
import wikipedia
from PyDictionary import PyDictionary
import os

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

    # Url which gives some json data about the joke
    randomJokeUrl = "https://official-joke-api.appspot.com/random_joke"

    # Converts the response to json
    jokeJSONData = requests.get(randomJokeUrl).json()

    # Setup and punchline are the 2 values of the joke
    setup = jokeJSONData["setup"]
    punchLine = jokeJSONData["punchline"]
    Speak(setup, 200)
    Speak(punchLine, 200)

# Function to get information from wikipedia
def SearchOnWikipedia(keyword):
    Speak(wikipedia.summary(keyword, sentences=2), 200)

# Function to tell a meaning of a word
def WhatIsTheMeaningOf(keyword):
    Speak(keyword + " is a " + str(PyDictionary.meaning(keyword)), 200)

# Opens a specified app
def OpenAPP(app):

    # Gets a list of all apps
    Applications = os.listdir("/Applications/")

    # Loops through all apps in the Applications list
    for _app in Applications:

        # finds the app
        if app.lower() in _app.lower():

            # Opens the app after formating it's path
            path = "'/Applications/" + _app + "'"
            os.system("open " + path)

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