import speech_recognition as sr
import pyttsx3

# Recognizer object
r = sr.Recognizer()

# Function to convert text to speech
def Speak(command):
    engine = pyttsx3.init()

    # Increasing the speed of voice (felt pretty slow on default)
    engine.setProperty('rate', 225)

    engine.say(command) 
    engine.runAndWait()

# print(sr.Microphone.list_microphone_names())

# Speak("Hello, my name is vision. How can I help you")

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
        Speak("did you say " + text)
