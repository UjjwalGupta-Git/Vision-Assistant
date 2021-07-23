pip uninstall pyaudio
pip3 uninstall pyaudio
brew uninstall portaudio
brew update
brew upgrade
python3 -m pip install --upgrade pip setuptools wheel
brew install portaudio --HEAD
python3 -m pip install pyaudio --global-option="build_ext" --global-option="-I/opt/homebrew/include" --global-option="-L/opt/homebrew/lib"
