import os
import json
import platform

dataJSON = open("bin/Data/Data.json", "r")
dataJSONObject = json.load(dataJSON)
dataJSON.close()

if(platform.system() == "Darwin"):
    Applications = os.listdir("/Applications/")
    dataJSONObject["MacApps"] = Applications
    dataJSON = open("bin/Data/Data.json", "w")
    json.dump(dataJSONObject, dataJSON)
    dataJSON.close()
elif(platform.system() == "Windows"):
    Applications = os.listdir("C://")
    dataJSONObject["WindowsApps"] = Applications
    dataJSON = open("bin/Data/Data.json", "w")
    json.dump(dataJSONObject, dataJSON)
    dataJSON.close()
