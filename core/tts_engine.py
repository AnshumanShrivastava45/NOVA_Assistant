import pyttsx3
import threading
import queue

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

speech_queue = queue.Queue()

lock = threading.Lock()


def tts_worker():

    while True:

        text = speech_queue.get()

        if text is None:
            break

        try:
            with lock:

                engine.stop()   
                engine.say(text)
                engine.runAndWait()

        except Exception as e:
            print("TTS Error:", e)


# start worker thread
threading.Thread(target=tts_worker, daemon=True).start()


def speak(text):

    speech_queue.put(text)

"""import pyttsx3
import threading

engine = pyttsx3.init()

engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)


def speak(text):

    def run():
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=run).start()"""