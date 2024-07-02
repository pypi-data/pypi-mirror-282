import platform
import os
import subprocess
import sys

def install_system_packages():
    system = platform.system()
    
    if system == 'Linux':
        command = 'sudo apt-get update && sudo apt-get install -y portaudio19-dev python3-pyaudio libasound2-dev libportaudio2 libportaudiocpp0'
    elif system == 'Darwin':
        command = 'brew install portaudio'
    elif system == 'Windows':
        command = f'{sys.executable} -m pip install pipwin && {sys.executable} -m pipwin install pyaudio'
    else:
        return "Unsupported OS"
    
    run_command(command)
    return "Done"

def install_library_packages():
    libraries=[
        "dill==0.3.8",
        "flask==3.0.3",
        "flask-cors==4.0.1",
        "gtts==2.5.1",
        "joblib==1.4.2",
        "moviepy==1.0.3",
        "nltk==3.8.1",
        "pyaudio==0.2.14",
        "pygame==2.5.2",
        "selenium==4.22.0",
        "setuptools==68.1.2",
        "sounddevice==0.4.7",
        "SpeechRecognition==3.10.4",
        "tensorflow==2.16.1",
        "tflearn==0.5.0",
        "twine==5.1.0",
        "wheel==0.43.0",
        "pycryptodome==3.20.0",
        "vosk==0.3.45",
        "tqdm==4.66.4",
        "pyttsx3==2.90",
        "requests==2.31.0",
    ]

    command = "pip install "
    for library in libraries:
        command += str(library) + " "
    run_command(command)
    
    return 'Done'

def upgrade_required_libraries():
    libraries=[
        "dill",
        "flask",
        "flask-cors",
        "gtts",
        "joblib",
        "moviepy",
        "nltk",
        "pyaudio",
        "pygame",
        "selenium",
        "setuptools",
        "sounddevice",
        "SpeechRecognition",
        "tensorflow",
        "tflearn",
        "twine",
        "wheel",
        "pycryptodome",
        "vosk",
        "tqdm",
        "pyttsx3",
        "requests",
    ]
    
    command = "pip install --upgrade "
    for library in libraries:
        command += library + " "
    run_command(command)
    
    return 'Done'

def upgrade_library():
    command = "pip install --upgrade YWP"
    run_command(command)
    
    return 'Done'

def get_terminal_command():
    if sys.platform.startswith('win'):
        return "cmd.exe"
    elif sys.platform.startswith('linux'):
        terminals = ["gnome-terminal", "xterm", "konsole", "xfce4-terminal", "lxterminal", "terminator", "tilix", "mate-terminal"]
        available_terminals = [term for term in terminals if os.system(f"which {term} > /dev/null 2>&1") == 0]
        if available_terminals:
            return available_terminals[0]
        else:
            return None
    elif sys.platform.startswith('darwin'):
        return "Terminal"
    else:
        return None

def run_command(command):
    terminal = get_terminal_command()
    if terminal:
        if terminal == "cmd.exe":
            os.system(f'start cmd /c "{command}"')
        elif terminal in ["gnome-terminal", "terminator", "tilix"]:
            os.system(f"{terminal} -- bash -c '{command}; read -p \"Press Enter to close...\"'")
        elif terminal == "konsole":
            os.system(f"{terminal} -e 'bash -c \"{command}; read -p \\\"Press Enter to close...\\\"\"'")
        elif terminal == "Terminal":
            os.system(f"open -a {terminal} '{command}'")
        else:
            os.system(f"{terminal} -hold -e 'bash -c \"{command}; read -p \\\"Press Enter to close...\\\"\"'")
    else:
        return "No supported terminal found."
