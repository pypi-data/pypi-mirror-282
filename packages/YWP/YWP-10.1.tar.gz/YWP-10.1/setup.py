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
    version='10.1',
    packages=find_packages(),
    install_requires=[
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
            # 'YWP.install_libraries=YWP:install_library_packages',
            'YWP.upgrade_libraries=YWP:upgrade_required_libraries',
            'YWP.upgrade_library=YWP:upgrade_library',
            'YWP=YWP:help',
            'YWP.help=YWP:help',
        ],
    },
)
