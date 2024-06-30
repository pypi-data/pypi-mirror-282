import os
import sys
from setuptools import setup, find_packages

def create_desktop_entry():
    home_dir = os.path.expanduser("~")
    project_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(project_dir, 'icon.png')
    exec_path = os.path.join(project_dir, 'ywp_script.py')

    desktop_entry_content = f"""
    [Desktop Entry]
    Version=1.0
    Name=YWP
    Comment=Your Wanted Products
    Exec=python3 {exec_path}
    Icon={icon_path}
    Terminal=false
    Type=Application
    Categories=Utility;
    """

    desktop_entry_path = os.path.join(home_dir, ".local", "share", "applications", "YWP.desktop")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(desktop_entry_path), exist_ok=True)

    # Create the .desktop file
    with open(desktop_entry_path, 'w') as f:
        f.write(desktop_entry_content)
    
    # Copy the icon to the applications directory
    os.system(f'cp {icon_path} {os.path.join(home_dir, ".local", "share", "applications", "icon.png")}')

if sys.platform.startswith('linux'):
    create_desktop_entry()

setup(
    name='YWP',
    version='2.4.0',
    packages=find_packages(),
    install_requires=[
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
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    package_data={
        '': ['icon.png', 'ywp_script.py'],
    },
    python_requires='>=3.6',
    description='This is a library to simplify the Python language for beginners while adding some features that are not found in other libraries',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Wanted Products (YWP)',
    author_email='pbstzidr@ywp.freewebhostmost.com',
    entry_points={
        'console_scripts': [
            'YWP.install_packages=YWP:install_system_packages',
        ],
    },
)
