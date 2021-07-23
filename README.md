# Vision-Assistant

This is an assistant that is currently under development. I will update `README.md` after changes start to happen.  

Run `scripts/MacOS/install_dependencies.sh` before running `src/main.py`

**NOTE:** You will need to Python3.9 installed. You can get it from https://www.python.org/downloads/
 
## Problems  

### 1. `bash: command not found: brew` or `zsh: command not found: brew` while running `install_dependencies.sh`  

**install homebrew through this command:**  
```  
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```  

### 2. pyaudio doesn't install while running `install_dependencies.sh`

**try:**  
```  
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```  
**or**  
```  
pip3 install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```  
### 3. If you are using a M1 mac and pyaudio doesn't install

Firstly check out this response from VikingOSX:  

https://discussions.apple.com/thread/252638887  

If the problem stil persists (which was the case for one of the collaborators):  

try running `scripts/MacOS/install_pyaudio_m1.sh`
