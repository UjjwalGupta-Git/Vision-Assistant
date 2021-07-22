# Vision-Assistant

This is an assistant that is currently under development,
I will update `README.md` after changes start to happen

You need homebrew to run `install_dependencies.sh`

The main file is `src/main.py`

## Problems

### pyaudio doesn't install while running `install_dependencies.sh`

**try:**  
```
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```  
**or**  
```
pip3 install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```  

### `bash: command not found: brew` or `zsh: command not found: brew`

**install homebrew through this command:**  
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
