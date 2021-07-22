from PyDictionary import PyDictionary
import possiblePhrases as pPhrases
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import wikipedia
import requests
import os

# Recognizer object
r = sr.Recognizer()

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

    # Gets a list of all apps
    Applications = os.listdir("/Applications/")

    # Loops through all apps in the Applications list
    for _app in Applications:

        # finds the app
        if app.lower() in _app.lower():

            # Opens the app after formating it's path
            path = "'/Applications/" + _app + "'"
            os.system("open " + path)

# Converts a list into string
def listToString(s):

    # Initialsing empty string
    tempStr = ""
    
    # every word in list "s" is being added to tempStr with space after each word
    for word in s: 
        tempStr += word + ' '
    
    return tempStr 

# This Function will take in the user's speech and perform other functions based on it
def DetectKeywords(sentence):

    # The 3 lines below take the string and removes the last word from it
    tempList = sentence.split(' ')
    tempList.pop()
    tempString = listToString(tempList).lower()

    # Debugging
    print(tempList)
    print(sentence.split(' ')[-1])

    # checks if the given sentence is in the "possibleJokeSentences" list in poosiblePhrases module (created by me)
    if(sentence in pPhrases.possibleJokeSentences):
        TellAJoke()

    # checks if the given sentence(excluding last word) is in the "possibleMeanings" list
    if(tempString in pPhrases.possibleMeanings):

        # Passes last word of the sentence
        WhatIsTheMeaningOf(sentence.split(' ')[-1])

    # checks if the given sentence(excluding last word) is in the "possibleAPP"
    if(tempString in pPhrases.possibleAPP):

        # Passes last word of the sentence
        OpenAPP(sentence.split(' ')[-1])

    # checks if the given sentence(excluding last word) is in the "possibleWikipedia"
    if(tempString in pPhrases.possibleWikipedia):

        # Passes last word of the sentence
        SearchOnWikipedia(sentence.split(' ')[-1])

while(True):
    with sr.Microphone() as source:

        print("calibrating for ambient noise")

        # Adjusts for ambient noise
        r.adjust_for_ambient_noise(source, duration=1)

        print("listening...")

        # Collects AudioData and stores it in audio variable
        audio = r.listen(source, timeout=5)

        # converts AudioData into text
        transcript = r.recognize_google(audio, language='en-US')

        DetectKeywords(transcript)
