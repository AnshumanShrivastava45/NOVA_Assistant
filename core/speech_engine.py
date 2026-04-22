import speech_recognition as sr
import requests

# Vosk imports
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json

recognizer = sr.Recognizer()

# 🔥 Load Vosk model (offline)
vosk_model = Model("vosk-model-small-en-us-0.15")


# 🌐 Check internet
def is_online():
    try:
        requests.get("https://google.com", timeout=2)
        return True
    except:
        return False


# 🎤 ONLINE (Google)
def take_command_online():

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:
        print("Recognizing (Online)...")
        command = recognizer.recognize_google(audio)

        print("User said:", command)
        return command.lower()

    except:
        return ""


# 🔊 OFFLINE (Vosk)
import numpy as np

def take_command_offline():

    print("Listening (Offline)...")

    rec = KaldiRecognizer(vosk_model, 16000)

    result_text = {"text": ""}   # 🔥 shared variable

    def callback(indata, frames, time, status):

        if rec.AcceptWaveform(indata.tobytes()):
            result = json.loads(rec.Result())
            text = result.get("text", "")

            if text:
                print("User said (Offline):", text)
                result_text["text"] = text

    with sd.InputStream(samplerate=16000,
                        blocksize=8000,
                        dtype='int16',
                        channels=1,
                        callback=callback):

        while True:
            if result_text["text"] != "":
                return result_text["text"].lower()

# 🔥 MAIN FUNCTION (AUTO SWITCH)
def take_command():

    if is_online():
        return take_command_online()
    else:
        return take_command_offline()




"""import speech_recognition as sr

recognizer = sr.Recognizer()

def take_command():

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)

        print("User said:", command)

        return command.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""
        """