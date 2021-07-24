from PyDictionary import PyDictionary
from playsound import playsound
from gtts import gTTS
import wikipedia
import requests
import platform
import os
import json

# Function to convert text to speech
def Speak(command):
    tts = gTTS(text=command, lang='en', slow=False)

    filename = "buffer.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# Function to tell a joke
def TellAJoke():

    # Url which gives some json data about the joke
    randomJokeUrl = "https://official-joke-api.appspot.com/random_joke"

    # Converts the response to json
    jokeJSONData = requests.get(randomJokeUrl).json()

    # Setup and punchline are the 2 values of the joke
    setup = jokeJSONData["setup"]
    punchLine = jokeJSONData["punchline"]
    Speak(setup)
    Speak(punchLine)

# Function to get information from wikipedia
def SearchOnWikipedia(keyword):
    Speak(wikipedia.summary(keyword, sentences=2))

# Function to tell a meaning of a word
def WhatIsTheMeaningOf(keyword):
    Speak(keyword + " is a " + str(PyDictionary.meaning(keyword)))

# Opens a specified app
def OpenAPP(app):

    # Opens the Data.json file
    with open("bin/Data/Data.json", 'r') as file:
        appList = json.load(file)


    if(platform.system() == "Windows"):

        # Loops through all apps in the Applications list
        for _app in appList["WindowsApps"]:

            # Finds the app
            if app.lower() in _app.lower() and ".exe" in _app.lower():

                # Opens the app
                os.system("start " + _app)
                break
    elif(platform.system() == "Darwin"):

        # Loops through all apps in the Applications list
        for _app in appList["MacApps"]:

            # Finds the app
            if app.lower() in _app.lower() and ".app" in _app.lower():

                # Opens the app
                os.system("open " + _app)
                break
