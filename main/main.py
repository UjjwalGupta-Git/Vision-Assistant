import possiblePhrases as pPhrases
import speech_recognition as sr
import speechFunctions as sF
import startup as st
import GUI
import multiprocessing

st.Initialise()

# Recognizer object
r = sr.Recognizer()

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
    print(sentence.split(' '))
    print(sentence.split(' ')[1:])
    print(listToString(sentence.split(' ')[1:]))
    print((listToString(sentence.split(' ')[1:]))[0:-1])
    print(tempList[0])

    # checks if the given sentence is in the "possibleJokeSentences" list in poosiblePhrases module (created by me)
    if(sentence in pPhrases.possibleJokeSentences):
        sF.TellAJoke()

    # checks if the given sentence(excluding last word) is in the "possibleMeanings" list
    if(tempString in pPhrases.possibleMeanings):

        # Passes last word of the sentence
        sF.WhatIsTheMeaningOf(sentence.split(' ')[-1])

    # checks if the given sentence(excluding last word) is in the "possibleAPP"
    if(tempList[0] + ' ' in pPhrases.possibleAPP):

        print("hi")
        # Passes last word of the sentence
        sF.OpenAPP((listToString(sentence.split(' ')[1:]))[0:-1])

    # checks if the given sentence(excluding last word) is in the "possibleWikipedia"
    if(tempString in pPhrases.possibleWikipedia):

        # Passes last word of the sentence
        sF.SearchOnWikipedia(sentence.split(' ')[-1])

DetectKeywords("launch system preferences")

while(True):
    with sr.Microphone() as source:

        print("calibrating for ambient noise")

        # Adjusts for ambient noise
        r.adjust_for_ambient_noise(source, duration=1)

        print("listening...")

        def Recognize():

            # Collects AudioData and stores it in audio variable
            audio = r.listen(source, timeout=5)

            # converts AudioData into text
            transcript = r.recognize_google(audio, language='en-US')

            DetectKeywords(transcript)

        def Audio():

            audio = r.listen(source, timeout=1)
            GUI.ProcessAudioData(audio)

        p1 =  multiprocessing.Process(target= Recognize)
        p2 =  multiprocessing.Process(target= Audio)
        p1.start()
        p2.start()
