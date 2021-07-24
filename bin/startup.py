# Changes to Data.json was stopped by this command
# git update-index --assume-unchanged bin/Data/Data.json

# To track changes again, use this command
# git update-index --no-assume-unchanged bin/Data/Data.json

import os
import json
import platform

# Loads the json file "Data.json" as read-only
dataJSON = open("bin/Data/Data.json", "r")
dataJSONObject = json.load(dataJSON)
dataJSON.close()

# Checks which operating system is MacOS
if(platform.system() == "Darwin"):

    # Find all applications and save them with thier path to Data.txt
    os.system("find /Applications -name '*.app' > bin/Data/Data.txt")
    os.system("find /System/Applications -name '*.app' >> bin/Data/Data.txt")

    # Opens the saved Data.txt file and assigns it to a variable
    tempData = ""
    with open("bin/Data/Data.txt", 'r') as file:
        tempData = file.read()
    
    # tempData has application paths divided by a new lines, this creates a list of all apps with thier paths
    Applications = tempData.split('\n')

    # This time it opens the "Data.json" as writable
    dataJSON = open("bin/Data/Data.json", "w")

    # Assigns the key of the value(MacApps) (Kind of like a dictionary)
    dataJSONObject["MacApps"] = Applications

    # Saves the data into Data.json and closes the files
    json.dump(dataJSONObject, dataJSON)
    dataJSON.close()
elif(platform.system() == "Windows"): # Checks if the operating system is Windows

    # Gets a list of all apps
    Applications = os.listdir("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\")

    # Adds path to each application
    i = 0
    for app in Applications:
        i += 1
        Applications[i] = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\" + app

    # This time it opens the "Data.json" as writable
    dataJSON = open("bin/Data/Data.json", "w")

    # Assigns the key of the value(WindowsApps) (Kind of like a dictionary)
    dataJSONObject["WindowsApps"] = Applications

    # Saves the data into Data.json and closes the files
    json.dump(dataJSONObject, dataJSON)
    dataJSON.close()
