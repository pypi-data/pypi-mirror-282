r"""
Created By Your Wanted Products (YWP)

Email: pbstzidr@ywp.freewebhostmost.com

Phone Number: +201096730619

WhatsApp Number: +201096730619

website: https://ywp.freewebhostmost.com
























"""

from flask import Flask

class server:

    def __init__(self):
        self.app = None

    def route_flask(self, location="", returnValue=""):

        app = self.app
        try:
            if app is None:
                app = Flask(__name__)

            def make_route(return_value):
                def route():
                    return return_value
                return route

            endpoint = location.strip('/')
            if endpoint == '':
                endpoint = 'index'

            app.add_url_rule(location, endpoint, make_route(returnValue))
            self.app = app
            return 'done'
        except Exception as error:
            raise error
        
    def run(self, check=False, debug=True, host="0.0.0.0", port="8000"):
        
        app = self.app
        try:
            if app is None:
                raise Exception("App not initialized")
            
            if check:
                if __name__ == "__main__":
                    app.run(debug=debug, host=host, port=port)
            else:
                app.run(debug=debug, host=host, port=port)
            return 'done'
        except Exception as error:
            raise error
        
class VideosCreator:
    
    class Basic:
        
        def basic_video_creator(image_folder="images/", animation_choice="None", frame_rate=25, video_name="output", video_type="mp4", video_platform="Youtube", image_time=5):
            
            import os
            from moviepy.editor import ImageClip, concatenate_videoclips
            from moviepy.video.fx import all as vfx

            VIDEO_DURATIONS = {
                'Youtube': 60,
                'Facebook': 20,
                'Instagram': 15,
                'Tiktok': 60
            }

            try:
                files = os.listdir(image_folder)
                image_files = [os.path.join(image_folder, f) for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                image_files.sort()
            except Exception as error:
                raise error

            if video_platform in VIDEO_DURATIONS:
                video_duration = VIDEO_DURATIONS[video_platform]
            else:
                raise ValueError(f"Unsupported video platform: {video_platform}. Choose from Youtube, Facebook, Instagram, or Tiktok.")

            video_clips = []
            for i, image_file in enumerate(image_files):
                clip = ImageClip(image_file).set_duration(image_time)
                video_clips.append(clip)
                
                if i < len(image_files) - 1 and animation_choice:
                    next_clip = ImageClip(image_files[i + 1]).set_duration(image_time)
                    if animation_choice == 'FadeIn':
                        fade_duration = min(1, image_time / 2)
                        video_clips.append(next_clip.crossfadein(fade_duration).set_start(clip.end))
                    elif animation_choice == 'FadeOut':
                        video_clips.append(clip.crossfadeout(1).set_end(clip.end))
                    elif animation_choice == 'Rotate':
                        rotate_clip = next_clip.rotate(lambda t: 360*t).set_start(clip.end)
                        video_clips.append(rotate_clip)
                    elif animation_choice == 'FlipHorizontal':
                        video_clips.append(next_clip.fx(vfx.mirror_x).set_start(clip.end))
                    elif animation_choice == 'FlipVertical':
                        video_clips.append(next_clip.fx(vfx.mirror_y).set_start(clip.end))
            
            final_video = concatenate_videoclips(video_clips, method="compose")
            
            output_file = f"{video_name}.{video_type}"
            final_video.write_videofile(output_file, fps=frame_rate)
            return 'done'

class Files:
    
    def open_file(filepath=""):
        import os
        import subprocess
        try:
            if os.path.exists(filepath):
                subprocess.Popen([str(filepath)])
                return "open"
            else:
                return "Not Found Path"
        except Exception as e:
            print ("An error occurred:", e)
            return "An error occurred:", e
   
    def create_file(name=""):

        print("Please enter the text or code (press Ctrl + D on Unix or Ctrl + Z then Enter on Windows to finish):")

        user_input_lines = []
        try:
            while True:
                line = input()
                user_input_lines.append(line)
        except EOFError:
            pass

        user_input = '\n'.join(user_input_lines)
        
        filename = name

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(user_input)
            return "created"
        except Exception as error:
            raise error

    def delete_all_files(directory=".", type={}):
        
        import os
        for filename in os.listdir(directory):
            for index, type in type.items():
                if filename.endswith((type)):
                    filepath = os.path.join(directory, filename)
                    try:
                        os.remove(filepath)
                        return "Deleted"
                    except Exception as error:
                        raise error
                
class endecrypt:
    
    class aes:
        def encrypt(file_path="", password=""):
            
            try:
                from Crypto.Util.Padding import pad
                from Crypto.Cipher import AES
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                cipher = AES.new(key, AES.MODE_CBC)
                ct_bytes = cipher.encrypt(pad(data, AES.block_size))
                result = cipher.iv + ct_bytes
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                raise e

        def decrypt(file_path="", password=""):

            try:
                from Crypto.Util.Padding import unpad
                from Crypto.Cipher import AES
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                iv = data[:16]
                ct = data[16:]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                result = unpad(cipher.decrypt(ct), AES.block_size)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                raise e 

    class BlowFish:
        def encrypt(file_path="", password=""):
            try:
                from Crypto.Cipher import Blowfish
                from Crypto.Util.Padding import pad
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                cipher = Blowfish.new(key, Blowfish.MODE_CBC)
                ct_bytes = cipher.encrypt(pad(data, Blowfish.block_size))
                result = cipher.iv + ct_bytes
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)

        def decrypt(file_path="", password=""):
            try:
                from Crypto.Cipher import Blowfish
                from Crypto.Util.Padding import unpad
                with open(file_path, 'rb') as f:
                    data = f.read()
                key = password.encode('utf-8').ljust(32, b'\0')
                iv = data[:8]
                ct = data[8:]
                cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
                result = unpad(cipher.decrypt(ct), Blowfish.block_size)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)

    class Base64:
        def encrypt(file_path=""):
            try:
                import base64
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = base64.b64encode(data)
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
            
        def decrypt(file_path=""):
            try:
                import base64
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = base64.b64decode(data)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
            
    class Hex:
        def encrypt(file_path=""):
            try:
                import binascii
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = binascii.hexlify(data)
                output_path = file_path + ".ywpdne"
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
            
        def decrypt(file_path=""):
            try:
                import binascii
                with open(file_path, 'rb') as f:
                    data = f.read()
                result = binascii.unhexlify(data)
                output_path = file_path.replace(".ywpdne", "")
                with open(output_path, 'wb') as f:
                    f.write(result)
                return 'done'
            except Exception as e:
                return str(e)
        
import os

class Libraries:
    
    class Basic:
        def init_creator(filesave="__init__.py", filename="", function_class=""):
            if filename == "" or function_class == "" or filesave == "":
                return "FileSave or FileName or Function/Class Name is Not Found"
            else:
                if os.path.exists(filesave):
                    try:
                        with open(filesave, "r") as f:
                            text = f.read()
                    except Exception as e:
                        return str(e)
                else:
                    text = ""
                try:
                    text += "\nfrom ." + filename + " import " + function_class
                    with open (filesave, "w") as f:
                        f.write(text)
                    return 'done'
                except Exception as e:
                    return str(e)
                
        def basic_setup_file_creator(filename="setup.py", folder_name="", readme_name="README.md", library_name="", library_version="", libraries_required=[], description="", creator_name="", creator_email="", License="MIT"):
            if License == "MIT":
                file_data = "from setuptools import setup, find_packages\n\nsetup(\nname='" + library_name + "',\nversion='" + library_version + "',\npackages=find_packages(),\ninstall_requires=" + str(libraries_required) + ",\nclassifiers=[\n'Programming Language :: Python :: 3',\n],\npython_requires='>=3.6',\ndescription='" + description + "',\nlong_description=open('" + readme_name + "').read(),\nlong_description_content_type='text/markdown',\nauthor='" + creator_name + "',\nauthor_email='" + creator_email + "',\n)"
                if os.path.exists(filename):
                    return 'FileName Found'
                else:
                    try:
                        with open (filename, "w") as f:
                            f.write(file_data)
                        return 'done'
                    except Exception as e:
                        return str(e)
            else:
                return 'Not From Licenses'
                    
        def upload_file_creator(filename="upload_libarary", pypi_api="", platform="windows"):
            platforms = ["windows", "linux"]
            if platform in platforms:
                if platform == "windows":
                    filename += ".bat"
                    file_data = "set TWINE_USERNAME=__token__\nset TWINE_PASSWORD=" + pypi_api + "/npython setup.py sdist bdist_wheel\nset TWINE_USERNAME=%TWINE_USERNAME% set TWINE_PASSWORD=%TWINE_PASSWORD% twine upload dist/*"
                    if os.path.exists(filename):
                        return 'FileName Found'
                    else:
                        try:
                            with open(filename, "w") as f:
                                f.write(file_data)
                            return 'done'
                        except Exception as e:
                            return str(e)
                elif platform == "linux":
                    filename += ".sh"
                    file_data = 'export TWINE_USERNAME="__token__"\nexport TWINE_PASSWORD="' + pypi_api + '"\npython setup.py sdist bdist_wheel\nTWINE_USERNAME="$TWINE_USERNAME" TWINE_PASSWORD="$TWINE_PASSWORD" twine upload dist/*'
                    if os.path.exists(filename):
                        return 'FileName Found'
                    else:
                        try:
                            with open(filename, "w") as f:
                                f.write(file_data)
                            return 'done'
                        except Exception as e:
                            return str(e)
                else:
                    return 'Platform Not Supported'
            else:
                return 'Platform Not Supported'

class Websites:
       
    def open_website(url=""):
        import webbrowser
        try:
            webbrowser.open(url)
            return "opened"
        except Exception as e:
            print ("An error occurred:", e)
            return "An error occurred:", e

class Audios:
    
    @staticmethod
    def ensure_model_exists():
        model_path = os.path.join(os.getcwd(), "model")
        if not os.path.exists(model_path):
            print("Model not found. Downloading model for en-US...")
            model_url = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
            model_file = "vosk-model-small-en-us-0.15.zip"
            model_extract_path = os.path.join(os.getcwd(), "model")
            Audios.download_and_extract(model_url, model_file, model_extract_path)
            print("Model downloaded and extracted.")
        else:
            print("Model already exists.")

    @staticmethod
    def download_and_extract(url, file_name, extract_to):
        import requests
        import shutil
        response = requests.get(url, stream=True)
        with open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        shutil.unpack_archive(file_name, extract_to)
        os.remove(file_name)

    @staticmethod
    def text_to_speech_offline(text="", filename="tts.mp3", language='en'):
        import pyttsx3
        engine = pyttsx3.init()
        engine.save_to_file(text, filename)
        engine.runAndWait()
        return "saved"

    @staticmethod
    def transcribe_audio_offline(filename="recorder.wav"):
        import wave
        from vosk import Model, KaldiRecognizer
        model_path = os.path.join(os.getcwd(), "model")
        model = Model(model_path)
        rec = KaldiRecognizer(model, 16000)
        wf = wave.open(filename, "rb")
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()
                return result
        final_result = rec.FinalResult()
        return final_result
        
    def play_audio(pro_path="", mp3_file_path=""):
        import os
        import subprocess
        if os.path.exists(mp3_file_path):
            subprocess.Popen([pro_path, mp3_file_path])
            return "opened"
        else:
            return "Not Found File"
        
    def play_sound(filename="tts.mp3"):
        import pygame
        pygame.mixer.init()
        sound = pygame.mixer.Sound(filename)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
        sound.stop()
        return "played"

    def play_audio_online(pro_path="", mp3_file_link=""):
            import subprocess
            subprocess.Popen([pro_path, mp3_file_link])
            return "opened"
        
    def record_audio(filename="recorder.wav", duration=5, fs=44100, device_number=2):
        import wave
        import sounddevice as sd
        sd.default.device = device_number
        try:
            audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()
            with wave.open(filename, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(fs)
                wf.writeframes(audio_data.tobytes())
            return "saved"
        except Exception as e:
            print ("An error occurred:", e)
            return "An error occurred:", e
        
    def transcribe_audio(filename="recorder.wav", language_="en-US"):
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)
            try:
                query = recognizer.recognize_google(audio, language=language_)
                return query
            except sr.UnknownValueError:
                return ""
            except sr.RequestError as e:
                print (f"Could not request results; {e}")
                return f"Could not request results; {e}"
            
    def stop_recording():
        import pyaudio
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            p.terminate()
            
    def text_to_speech(text="", filename="tts.mp3", language='en'):
        from gtts import gTTS
        tts = gTTS(text, lang=language)
        tts.save(filename)
        return "saved"

class System:
        
    def hibernate():
        import os
        import platform
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /h")
        else:
            raise NotImplementedError("Unsupported OS")

    def restart():
        import os
        import platform
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /r /t 1")
        else:
            raise NotImplementedError("Unsupported OS")

    def shutdown():
        import platform
        import subprocess
        system = platform.system()
        if system == "Windows":
            subprocess.run(["shutdown", "/s", "/t", "1"])
        elif system == "Linux" or system == "Darwin":
            subprocess.run(["sudo", "shutdown", "-h", "now"])
        else:
            raise NotImplementedError("Unsupported OS")
        
    def log_off():
        import os
        import platform
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /l")
        else:
            raise NotImplementedError("Unsupported OS")

class Crypto:

    def token_information(data="", type='binance'):
        if type == 'binance':
            link = "https://bscscan.com/token/" + str(data)
            Websites.open_website(link)
            return "opened"
        elif type == 'etherum':
            link = "https://etherscan.io/token/" + str(data)
            Websites.open_website(link)
            return "opened"
        elif type == 'geckoterminal':
            link = 'https://ywp.freewebhostmost.com/really/token.php?pool=' + str(data)
            return "opened"
        else:
            return "UnSupported type"
    
class AI:
    class Builder:
        def __init__(self):
            self.intents = []
            
        def json_creator(self, jsonfile="intents.json", tag="", patterns=[], responses=[]):
            import json
            intents = self.intents

            intents.append({
                "tag": tag,
                "patterns": patterns,
                "responses": responses
            })

            with open(jsonfile, 'w', encoding='utf-8') as f:
                json.dump({"intents": intents}, f, indent=4, ensure_ascii=False)

        def train(self, jsonfile="intents.json", picklefile="data.pickle", h5file="model.h5"):
            import nltk
            from nltk.stem.lancaster import LancasterStemmer
            import numpy as np
            import tensorflow as tf
            from tensorflow.keras.models import Sequential
            from tensorflow.keras.layers import Dense
            import json
            import pickle

            nltk.download('punkt')
            stemmer = LancasterStemmer()

            try:
                with open(jsonfile, encoding='utf-8') as file:
                    data = json.load(file)
            except:
                return 'error:jsonnotfound'

            try:
                with open(picklefile, "rb") as f:
                    words, labels, training, output = pickle.load(f)
            except:
                words = []
                labels = []
                docs_x = []
                docs_y = []
                for intent in data["intents"]:
                    for pattern in intent["patterns"]:
                        wrds = nltk.word_tokenize(pattern)
                        words.extend(wrds)
                        docs_x.append(wrds)
                        docs_y.append(intent["tag"])

                    if intent["tag"] not in labels:
                        labels.append(intent["tag"])

                words = [stemmer.stem(w.lower()) for w in words if w != "?"]
                words = sorted(list(set(words)))

                labels = sorted(labels)

                training = []
                output = []

                out_empty = [0 for _ in range(len(labels))]

                for x, doc in enumerate(docs_x):
                    bag = []

                    wrds = [stemmer.stem(w) for w in doc]

                    for w in words:
                        if w in wrds:
                            bag.append(1)
                        else:
                            bag.append(0)

                    output_row = out_empty[:]
                    output_row[labels.index(docs_y[x])] = 1

                    training.append(bag)
                    output.append(output_row)

                training = np.array(training)
                output = np.array(output)

                with open(picklefile, "wb") as f:
                    pickle.dump((words, labels, training, output), f)

            model = Sequential()
            model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
            model.add(Dense(8, activation='relu'))
            model.add(Dense(len(output[0]), activation='softmax'))

            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

            try:
                model.load_weights(h5file)
            except:
                model.fit(training, output, epochs=1000, batch_size=8, verbose=1)
                model.save(h5file)

            return 'done'
        
        @staticmethod
        def bag_of_words(s, words):
            import nltk
            from nltk.stem.lancaster import LancasterStemmer
            nltk.download('punkt')
            stemmer = LancasterStemmer()
            import numpy as np

            bag = [0 for _ in range(len(words))]

            s_words = nltk.word_tokenize(s)
            s_words = [stemmer.stem(word.lower()) for word in s_words]

            for se in s_words:
                for i, w in enumerate(words):
                    if w == se:
                        bag[i] = 1

            return np.array(bag)

        def process(self, message="", picklefile="data.pickle", h5file="model.h5", jsonfile="intents.json", sleeptime=0):
            import nltk
            from nltk.stem.lancaster import LancasterStemmer
            nltk.download('punkt')
            stemmer = LancasterStemmer()

            import numpy as np
            import tensorflow as tf
            from tensorflow.keras.models import Sequential
            from tensorflow.keras.layers import Dense
            import random
            import json
            import pickle
            from time import sleep

            try:
                with open(jsonfile, encoding='utf-8') as file:
                    data = json.load(file)
            except:
                return 'error:jsonnotfound'

            try:
                with open(picklefile, "rb") as f:
                    words, labels, training, output = pickle.load(f)
            except:
                return 'error:picklenotfound'

            model = Sequential()
            model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
            model.add(Dense(8, activation='relu'))
            model.add(Dense(len(output[0]), activation='softmax'))

            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

            try:
                model.load_weights(h5file)
            except:
                return 'h5notfound'

            bag = self.bag_of_words(message, words)
            results = model.predict(np.array([bag]))[0]
            results_index = np.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.8:
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                sleep(sleeptime)
                Bot = random.choice(responses)
                return Bot
            else:
                return "I don't understand!"

class inuser:
    class Audios:
        def play_sound_inuser():
            filename = input("Enter FileName: ")
            import pygame
            pygame.mixer.init()
            sound = pygame.mixer.Sound(filename)
            sound.play()
            while pygame.mixer.get_busy():
                pygame.time.Clock().tick(10)
            sound.stop()
            return "played"
        
        def play_audio_inuser():
            pro_path = input("Enter Program Path: ")
            mp3_file_path = input("Enter MP3 File Path: ")
            import os
            import subprocess
            if os.path.exists(mp3_file_path):
                subprocess.Popen([pro_path, mp3_file_path])
                return "opened"
            else:
                return "Not Found File"
            
        def record_audio_inuser():
            filename = input("Enter FileName: ")
            duration = int(input("Enter Duration Time: "))
            fs = int(input("Enter FS Number: "))
            device_number = int(input("Enter Device Number"))
            import wave
            import sounddevice as sd
            sd.default.device = device_number
            try:
                audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
                sd.wait()
                with wave.open(filename, 'wb') as wf:
                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(fs)
                    wf.writeframes(audio_data.tobytes())
                return "saved"
            except Exception as e:
                print ("An error occurred:", e)
                return "An error occurred:", e
            
        def transcribe_audio_offline_inuser():
            filename = input("Enter FileName: ")
            import wave
            from vosk import Model, KaldiRecognizer
            model_path = os.path.join(os.getcwd(), "model")
            model = Model(model_path)
            rec = KaldiRecognizer(model, 16000)
            wf = wave.open(filename, "rb")
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    return result
            final_result = rec.FinalResult()
            return final_result
        
        def transcribe_audio_inuser():
            filename = input("Enter FileName: ")
            language_ = input("Enter Language: ")
            import speech_recognition as sr
            recognizer = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                audio = recognizer.record(source)
                try:
                    query = recognizer.recognize_google(audio, language=language_)
                    return query
                except sr.UnknownValueError:
                    return ""
                except sr.RequestError as e:
                    print (f"Could not request results; {e}")
                    return f"Could not request results; {e}"
                
        def text_to_speech_inuser():
            text = input("Enter Text: ")
            filename = input("Enter FileName: ")
            language = input("Enter Language: ")
            from gtts import gTTS
            tts = gTTS(text, lang=language)
            tts.save(filename)
            return "saved"
        
        def text_to_speech_offline_inuser():
            text = input("Enter Text: ")
            filename = input("Enter FileName: ")
            import pyttsx3
            engine = pyttsx3.init()
            engine.save_to_file(text, filename)
            engine.runAndWait()
            return "saved"
        
        def play_audio_online_inuser():
            pro_path = input("Enter Program Path: ")
            mp3_file_link = input("Enter MP3 File Link: ")
            import subprocess
            subprocess.Popen([pro_path, mp3_file_link])
            return "opened"
        
    class Files:
        def create_file_inuser():
            name = input("Enter FileName: ")

            print("Please enter the text or code (press Ctrl + D on Unix or Ctrl + Z then Enter on Windows to finish):")

            user_input_lines = []
            try:
                while True:
                    line = input()
                    user_input_lines.append(line)
            except EOFError:
                pass

            user_input = '\n'.join(user_input_lines)
            
            filename = name

            try:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(user_input)
                return "created"
            except Exception as error:
                raise error
            
        def open_file_inuser():
            filepath = input("Enter FilePath: ")
            import os
            import subprocess
            try:
                if os.path.exists(filepath):
                    subprocess.Popen([str(filepath)])
                    return "open"
                else:
                    return "Not Found Path"
            except Exception as e:
                print ("An error occurred:", e)
                return "An error occurred:", e
            
        def delete_all_files_inuser():
            directory = input("Enter Directory/Folder: ")
            type = input("Enter Type: ")
        
            import os
            for filename in os.listdir(directory):
                for index, type in type.items():
                    if filename.endswith((type)):
                        filepath = os.path.join(directory, filename)
                        try:
                            os.remove(filepath)
                            return "Deleted"
                        except Exception as error:
                            raise error
                        
    class Websites:
       
        def open_website_inuser():
            url = input("Enter URL: ")
            import webbrowser
            try:
                webbrowser.open(url)
                return "opened"
            except Exception as e:
                print ("An error occurred:", e)
                return "An error occurred:", e
            
    class Crypto:

        def token_information_inuser():
            data = input("Enter Data: ")
            type = input("Enter Type: ")
            if type == 'binance':
                link = "https://bscscan.com/token/" + str(data)
                Websites.open_website(link)
                return "opened"
            elif type == 'etherum':
                link = "https://etherscan.io/token/" + str(data)
                Websites.open_website(link)
                return "opened"
            elif type == 'geckoterminal':
                link = 'https://ywp.freewebhostmost.com/really/token.php?pool=' + str(data)
                return "opened"
            else:
                return "UnSupported type"
            
    class server:

        def __init__(self):
            self.app = None

        def route_flask_inuser(self):
            location = input("Enter Location: ")
            returnValue = input("Enter returnValue: ")

            app = self.app
            try:
                if app is None:
                    app = Flask(__name__)

                def make_route(return_value):
                    def route():
                        return return_value
                    return route

                endpoint = location.strip('/')
                if endpoint == '':
                    endpoint = 'index'

                app.add_url_rule(location, endpoint, make_route(returnValue))
                self.app = app
                return 'done'
            except Exception as error:
                raise error
            
        def run_inuser(self):
            check = bool(input("Enter check: "))
            debug = bool(input("Enter Debug: "))
            host = input("Enter Host: ")
            port = input("Enter Port: ")
            
            app = self.app
            try:
                if app is None:
                    raise Exception("App not initialized")
                
                if check:
                    if __name__ == "__main__":
                        app.run(debug=debug, host=host, port=port)
                else:
                    app.run(debug=debug, host=host, port=port)
                return 'done'
            except Exception as error:
                raise error
            
    class AI:
        class Builder:
            def __init__(self):
                self.intents = []
                
            def json_creator_inuser(self):
                jsonfile = input("Enter JsonFile Name/Path: ")
                tag = input("Enter tag: ")
                patterns = input("Enter Patterns (,): ").split(",")
                responses = input("Enter Responses (,): ").split(",")
                
                import json
                intents = self.intents

                intents.append({
                    "tag": tag,
                    "patterns": patterns,
                    "responses": responses
                })

                with open(jsonfile, 'w', encoding='utf-8') as f:
                    json.dump({"intents": intents}, f, indent=4, ensure_ascii=False)

            def train_inuser(self):
                jsonfile = input("Enter JsonFile Name/Path: ")
                picklefile = input("Enter PickleFile Name/Path: ")
                h5file = input("Enter H5File Name/Path: ")
                
                import nltk
                from nltk.stem.lancaster import LancasterStemmer
                import numpy as np
                import tensorflow as tf
                from tensorflow.keras.models import Sequential
                from tensorflow.keras.layers import Dense
                import json
                import pickle

                nltk.download('punkt')
                stemmer = LancasterStemmer()

                try:
                    with open(jsonfile, encoding='utf-8') as file:
                        data = json.load(file)
                except:
                    return 'error:jsonnotfound'

                try:
                    with open(picklefile, "rb") as f:
                        words, labels, training, output = pickle.load(f)
                except:
                    words = []
                    labels = []
                    docs_x = []
                    docs_y = []
                    for intent in data["intents"]:
                        for pattern in intent["patterns"]:
                            wrds = nltk.word_tokenize(pattern)
                            words.extend(wrds)
                            docs_x.append(wrds)
                            docs_y.append(intent["tag"])

                        if intent["tag"] not in labels:
                            labels.append(intent["tag"])

                    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
                    words = sorted(list(set(words)))

                    labels = sorted(labels)

                    training = []
                    output = []

                    out_empty = [0 for _ in range(len(labels))]

                    for x, doc in enumerate(docs_x):
                        bag = []

                        wrds = [stemmer.stem(w) for w in doc]

                        for w in words:
                            if w in wrds:
                                bag.append(1)
                            else:
                                bag.append(0)

                        output_row = out_empty[:]
                        output_row[labels.index(docs_y[x])] = 1

                        training.append(bag)
                        output.append(output_row)

                    training = np.array(training)
                    output = np.array(output)

                    with open(picklefile, "wb") as f:
                        pickle.dump((words, labels, training, output), f)

                model = Sequential()
                model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
                model.add(Dense(8, activation='relu'))
                model.add(Dense(len(output[0]), activation='softmax'))

                model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

                try:
                    model.load_weights(h5file)
                except:
                    model.fit(training, output, epochs=1000, batch_size=8, verbose=1)
                    model.save(h5file)

                return 'done'

            def process_inuser(self):
                message = input("Enter Message: ")
                picklefile = input("Enter PickleFile Name/Path: ")
                h5file = input("Enter H5File Name/Path: ")
                jsonfile = input("Enter JsonFile Name/Path: ")
                sleeptime = int(input("Enter Sleep Time: "))
                
                import nltk
                from nltk.stem.lancaster import LancasterStemmer
                nltk.download('punkt')
                stemmer = LancasterStemmer()

                import numpy as np
                import tensorflow as tf
                from tensorflow.keras.models import Sequential
                from tensorflow.keras.layers import Dense
                import random
                import json
                import pickle
                from time import sleep

                try:
                    with open(jsonfile, encoding='utf-8') as file:
                        data = json.load(file)
                except:
                    return 'error:jsonnotfound'

                try:
                    with open(picklefile, "rb") as f:
                        words, labels, training, output = pickle.load(f)
                except:
                    return 'error:picklenotfound'

                model = Sequential()
                model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
                model.add(Dense(8, activation='relu'))
                model.add(Dense(len(output[0]), activation='softmax'))

                model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

                try:
                    model.load_weights(h5file)
                except:
                    return 'h5notfound'

                ai = AI.Builder()
                bag = ai.bag_of_words(message, words)
                results = model.predict(np.array([bag]))[0]
                results_index = np.argmax(results)
                tag = labels[results_index]
                if results[results_index] > 0.8:
                    for tg in data["intents"]:
                        if tg['tag'] == tag:
                            responses = tg['responses']
                    sleep(sleeptime)
                    Bot = random.choice(responses)
                    return Bot
                else:
                    return "I don't understand!"
    
    class VideosCreator:
    
        class Basic:
            
            def basic_video_creator_inuser():
                image_folder = input("Enter Image Folder Name/Path: ")
                animation_choice = input("Enter Animation: ")
                frame_rate = int(input("Enter Frame Rate: "))
                video_name = input("Enter Video Name: ")
                video_type = input("Enter Video Type: ")
                video_platform = input("Enter Video Platform: ")
                image_time = int(input("Enter Image Time: "))
                
                import os
                from moviepy.editor import ImageClip, concatenate_videoclips
                from moviepy.video.fx import all as vfx

                VIDEO_DURATIONS = {
                    'Youtube': 60,
                    'Facebook': 20,
                    'Instagram': 15,
                    'Tiktok': 60
                }

                try:
                    files = os.listdir(image_folder)
                    image_files = [os.path.join(image_folder, f) for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                    image_files.sort()
                except Exception as error:
                    raise error

                if video_platform in VIDEO_DURATIONS:
                    video_duration = VIDEO_DURATIONS[video_platform]
                else:
                    raise ValueError(f"Unsupported video platform: {video_platform}. Choose from Youtube, Facebook, Instagram, or Tiktok.")

                video_clips = []
                for i, image_file in enumerate(image_files):
                    clip = ImageClip(image_file).set_duration(image_time)
                    video_clips.append(clip)
                    
                    if i < len(image_files) - 1 and animation_choice:
                        next_clip = ImageClip(image_files[i + 1]).set_duration(image_time)
                        if animation_choice == 'FadeIn':
                            fade_duration = min(1, image_time / 2)
                            video_clips.append(next_clip.crossfadein(fade_duration).set_start(clip.end))
                        elif animation_choice == 'FadeOut':
                            video_clips.append(clip.crossfadeout(1).set_end(clip.end))
                        elif animation_choice == 'Rotate':
                            rotate_clip = next_clip.rotate(lambda t: 360*t).set_start(clip.end)
                            video_clips.append(rotate_clip)
                        elif animation_choice == 'FlipHorizontal':
                            video_clips.append(next_clip.fx(vfx.mirror_x).set_start(clip.end))
                        elif animation_choice == 'FlipVertical':
                            video_clips.append(next_clip.fx(vfx.mirror_y).set_start(clip.end))
                
                final_video = concatenate_videoclips(video_clips, method="compose")
                
                output_file = f"{video_name}.{video_type}"
                final_video.write_videofile(output_file, fps=frame_rate)
                return 'done'
            
    class endecrypt:

        class aes:
            def encrypt_inuser():
                file_path = input("Enter File Path: ")
                password = input("Enter Password: ")
                
                try:
                    from Crypto.Util.Padding import pad
                    from Crypto.Cipher import AES
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    key = password.encode('utf-8').ljust(32, b'\0')
                    cipher = AES.new(key, AES.MODE_CBC)
                    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
                    result = cipher.iv + ct_bytes
                    output_path = file_path + ".ywpdne"
                    with open(output_path, 'wb') as f:
                        f.write(result)
                    return 'done'
                except Exception as e:
                    raise e

            def decrypt_inuser():
                file_path = input("Enter File Path: ")
                password = input("Enter Password: ")

                try:
                    from Crypto.Util.Padding import unpad
                    from Crypto.Cipher import AES
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    key = password.encode('utf-8').ljust(32, b'\0')
                    iv = data[:16]
                    ct = data[16:]
                    cipher = AES.new(key, AES.MODE_CBC, iv)
                    result = unpad(cipher.decrypt(ct), AES.block_size)
                    output_path = file_path.replace(".ywpdne", "")
                    with open(output_path, 'wb') as f:
                        f.write(result)
                    return 'done'
                except Exception as e:
                    raise e 

        class BlowFish:
            def encrypt_inuser():
                file_path = input("Enter File Path: ")
                password = input("Enter Password: ")
                
                try:
                    from Crypto.Cipher import Blowfish
                    from Crypto.Util.Padding import pad
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    key = password.encode('utf-8').ljust(32, b'\0')
                    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
                    ct_bytes = cipher.encrypt(pad(data, Blowfish.block_size))
                    result = cipher.iv + ct_bytes
                    output_path = file_path + ".ywpdne"
                    with open(output_path, 'wb') as f:
                        f.write(result)
                    return 'done'
                except Exception as e:
                    return str(e)

            def decrypt_inuser():
                file_path = input("Enter File Path: ")
                password = input("Enter Password: ")
                
                try:
                    from Crypto.Cipher import Blowfish
                    from Crypto.Util.Padding import unpad
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    key = password.encode('utf-8').ljust(32, b'\0')
                    iv = data[:8]
                    ct = data[8:]
                    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
                    result = unpad(cipher.decrypt(ct), Blowfish.block_size)
                    output_path = file_path.replace(".ywpdne", "")
                    with open(output_path, 'wb') as f:
                        f.write(result)
                    return 'done'
                except Exception as e:
                    return str(e)

        class Base64:
            def encrypt_inuser():
                file_path = input("Enter File Path: ")
                
                try:
                    import base64
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    result = base64.b64encode(data)
                    output_path = file_path + ".ywpdne"
                    with open(output_path, 'wb') as f:
                        f.write(result)
                    return 'done'
                except Exception as e:
                    return str(e)
                
            def decrypt_inuser():
                file_path = input("Enter File Path: ")
                
                try:
                    import base64
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    result = base64.b64decode(data)
                    output_path = file_path.replace(".ywpdne", "")
                    with open(output_path, 'wb') as f:
                        f.write(result)
                    return 'done'
                except Exception as e:
                    return str(e)
                
        class Hex:
            def encrypt_inuser():
                file_path = input("Enter File Path: ")
                
                try:
                    import binascii
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    result = binascii.hexlify(data)
                    output_path = file_path + ".ywpdne"
                    with open(output_path, 'wb') as f:
                        f.write(result)
                    return 'done'
                except Exception as e:
                    return str(e)
                
            def decrypt_inuser():
                file_path = input("Enter File Path: ")
                
                try:
                    import binascii
                    with open(file_path, 'rb') as f:
                        data = f.read()
                    result = binascii.unhexlify(data)
                    output_path = file_path.replace(".ywpdne", "")
                    with open(output_path, 'wb') as f:
                        f.write(result)
                    return 'done'
                except Exception as e:
                    return str(e)
                
    class Libraries:
    
        class Basic:
            def init_creator_inuser():
                filesave = input("Enter File Save: ")
                filename = input("Enter File Name: ")
                function_class = input("Enter Function/Class Name: ")
                
                if filename == "" or function_class == "" or filesave == "":
                    return "FileSave or FileName or Function/Class Name is Not Found"
                else:
                    if os.path.exists(filesave):
                        try:
                            with open(filesave, "r") as f:
                                text = f.read()
                        except Exception as e:
                            return str(e)
                    else:
                        text = ""
                    try:
                        text += "\nfrom ." + filename + " import " + function_class
                        with open (filesave, "w") as f:
                            f.write(text)
                        return 'done'
                    except Exception as e:
                        return str(e)
                    
            def basic_setup_file_creator_inuser():
                filename = input("Enter File Name: ")
                folder_name = input("Enter Folder Name: ")
                readme_name = input("Enter Read Me File Name: ")
                library_name = input("Enter Library Name: ")
                library_version = input("Enter Library Version: ")
                libraries_required = input("Enter Libraries Required (,): ").split(",")
                description = input("Enter Description: ")
                creator_name = input("Enter Creator Name: ")
                creator_email = input("Enter Creator Email: ")
                License = input("Enter License: ")
                
                if License == "MIT":
                    file_data = "from setuptools import setup, find_packages\n\nsetup(\nname='" + library_name + "',\nversion='" + library_version + "',\npackages=find_packages(),\ninstall_requires=" + str(libraries_required) + ",\nclassifiers=[\n'Programming Language :: Python :: 3',\n],\npython_requires='>=3.6',\ndescription='" + description + "',\nlong_description=open('" + readme_name + "').read(),\nlong_description_content_type='text/markdown',\nauthor='" + creator_name + "',\nauthor_email='" + creator_email + "',\n)"
                    if os.path.exists(filename):
                        return 'FileName Found'
                    else:
                        try:
                            with open (filename, "w") as f:
                                f.write(file_data)
                            return 'done'
                        except Exception as e:
                            return str(e)
                else:
                    return 'Not From Licenses'
                        
            def upload_file_creator_inuser():
                filename = input("Enter File Name: ")
                pypi_api = input("Enter PyPi API: ")
                platform = input("Enter Platform: ")
                
                platforms = ["windows", "linux"]
                if platform in platforms:
                    if platform == "windows":
                        filename += ".bat"
                        file_data = "set TWINE_USERNAME=__token__\nset TWINE_PASSWORD=" + pypi_api + "/npython setup.py sdist bdist_wheel\nset TWINE_USERNAME=%TWINE_USERNAME% set TWINE_PASSWORD=%TWINE_PASSWORD% twine upload dist/*"
                        if os.path.exists(filename):
                            return 'FileName Found'
                        else:
                            try:
                                with open(filename, "w") as f:
                                    f.write(file_data)
                                return 'done'
                            except Exception as e:
                                return str(e)
                    elif platform == "linux":
                        filename += ".sh"
                        file_data = 'export TWINE_USERNAME="__token__"\nexport TWINE_PASSWORD="' + pypi_api + '"\npython setup.py sdist bdist_wheel\nTWINE_USERNAME="$TWINE_USERNAME" TWINE_PASSWORD="$TWINE_PASSWORD" twine upload dist/*'
                        if os.path.exists(filename):
                            return 'FileName Found'
                        else:
                            try:
                                with open(filename, "w") as f:
                                    f.write(file_data)
                                return 'done'
                            except Exception as e:
                                return str(e)
                    else:
                        return 'Platform Not Supported'
                else:
                    return 'Platform Not Supported'

from .packlib import install_system_packages
# from .packlib import install_library_packages
from .packlib import get_terminal_command
from .packlib import run_command
from .packlib import upgrade_required_libraries
from .packlib import upgrade_library
from .ywp import help

