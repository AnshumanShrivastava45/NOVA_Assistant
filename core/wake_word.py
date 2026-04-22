import speech_recognition as sr
import requests

from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json

recognizer = sr.Recognizer()

vosk_model = Model("vosk-model-small-en-us-0.15")


def is_online():
    try:
        requests.get("https://google.com", timeout=2)
        return True
    except:
        return False


# 🔊 OFFLINE wake word
def detect_wake_word_offline():

    print("Waiting for wake word (Offline)...")

    rec = KaldiRecognizer(vosk_model, 16000)

    with sd.RawInputStream(samplerate=16000,
                           blocksize=8000,
                           dtype='int16',
                           channels=1) as stream:

        while True:
            data, _ = stream.read(4000)   
            data = bytes(data) 
            
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")

                print("Heard (Offline):", text)

                if "nova" in text:
                    return True


def detect_wake_word_online():

    with sr.Microphone() as source:

        print("Waiting for wake word...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()

        print("Heard:", text)

        if "nova" in text:
            return True

    except:
        pass

    return False


def detect_wake_word():

    if is_online():
        return detect_wake_word_online()
    else:
        return detect_wake_word_offline()
    
    





"""import speech_recognition as sr

recognizer = sr.Recognizer()

def detect_wake_word():

    with sr.Microphone() as source:

        print("Waiting for wake word...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio).lower()

        print("Heard:", text)

        # flexible detection
        if "nova" in text:
            return True

    except:
        pass

    return False"""