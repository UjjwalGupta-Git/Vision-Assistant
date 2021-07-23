import subprocess
import sys

dependencies = {
    "pyaudio",
    "SpeechRecognition",
    "requests",
    "wikipedia",
    "pydictionary",
    "gtts",
    "playsound"
}

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for module in dependencies:
    install(module)