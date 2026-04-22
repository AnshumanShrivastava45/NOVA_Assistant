import time
from core.tts_engine import speak
from core.speech_engine import take_command
from core.intent_classifier import predict_intent
from core.command_router import execute_intent


def start_assistant(gui):
 
    gui.status.setText("Assistant Activated")
    speak("Hello, how can I assist you today?")

    while True:
        
        gui.status.setText("Listening...")
        time.sleep(1)

        command = take_command()


        command = command.replace("nova", "").strip()

        if command == "":
            continue

        gui.status.setText("Recognizing...")
        time.sleep(1)
        
        gui.status.setText(f"You said: {command}")

        intent, confidence = predict_intent(command)
        print("Intent:", intent)

       #gui.status.setText(f"Intent: {intent}")
        execute_intent(intent, command,gui)
        

        if intent == "ai_mode":
            time.sleep(2)
        else:
            time.sleep(10)

      
        

        