from click import command

from features.system_commands import brightness_down, brightness_up, get_memory, lock_system, mute, open_application, open_folder, save_memory, search_google, shutdown_pc, restart_pc, take_screenshot, volume_down, volume_up, search_file_windows, wifi_off, wifi_on
from features.ai_mode import get_ai_response
from core.tts_engine import speak
from features.emotion_detector import detect_emotion
from features.music_recommender import recommend_music
import sys


ai_mode = False


def execute_intent(intent, command, gui):

    global ai_mode

    command = command.lower()

    # EXIT AI MODE
    if "system mode" in command or "system mod" in command or "exit ai mode" in command:
        ai_mode = False
        gui.status.setText("System Mode Activated")
        speak("System mode activated")
        return
    
    if "nova close" in command or "close assistant" in command or intent == "close_assistant":
        gui.status.setText("Closing assistant")
        speak("Goodbye")
        sys.exit()
    
    if "remember" in command:
        intent = "remember"


    if "what did i tell you" in command:
        intent = "recall_memory"


    # ENTER AI MODE
    if "ai mode" in command or intent == "ai_mode":
        ai_mode = True
        gui.status.setText("AI Mode Activated")
        speak("AI mode activated")
        return

    if ai_mode:
        response = get_ai_response(command)
        clean_text = response.replace("**", "")
        gui.status.setText(clean_text)
        speak(clean_text)
        return

    # SYSTEM COMMANDS
    if intent == "open_browser":
        open_application("chrome")
        gui.status.setText("Opening Chrome")
        speak("Opening Chrome")

    elif intent == "shutdown_pc":
        shutdown_pc()
        gui.status.setText("Shutting down system")

    elif intent == "restart_pc":
        restart_pc()
        gui.status.setText("Restarting system")

    elif intent == "open_app":

        words = command.split()

        if len(words) >= 2:
            app_name = words[-1]
            open_application(app_name)
            gui.status.setText(f"Opening {app_name}")
            speak(f"Opening {app_name}")
    
    elif intent == "music_recommend":
        gui.status.setText("Detecting your emotion...")
        speak("Detecting your emotion")

        emotion = detect_emotion()
        gui.status.setText(f"Emotion detected: {emotion}")
        speak(f"You seem {emotion}. Playing music for you")

        recommend_music(emotion)

    elif intent == "screenshot":
        take_screenshot()
        gui.status.setText("Screenshot taken")
        speak("Screenshot taken")


    elif intent == "open_folder":
        open_folder(command, gui)
        speak("Opening folder")
    
    elif intent == "lock_system":
        lock_system()
        gui.status.setText("Locking system")
        speak("Locking system")
        

    elif intent == "volume_up":
        volume_up()
        gui.status.setText("Volume up")
        speak("Volume up")
    
    elif intent == "volume_down":
        volume_down()
        gui.status.setText("Volume down")
        speak("Volume down")

    elif intent == "mute":
        mute()
        gui.status.setText("Muting volume")
        speak("Muting volume")

    elif intent == "remember":
        text = command.replace("remember", "").strip()

        if len(text) < 3:
          gui.status.setText("What should I remember?")
          speak("What should I remember?")
          return
        
        save_memory(text)
        gui.status.setText("I will remember that")
        speak("I will remember that")
        print("Speaking:", text)


    elif intent == "recall_memory":
        data = get_memory()
        gui.status.setText(data)
        speak(data)

    elif intent == "google_search":
        query = command.replace("search", "")
        search_google(query)

    elif intent == "search_file":
        filename = command.replace("search file", "").strip()
        gui.status.setText(f"Searching {filename}")
        speak(f"Searching for {filename}")
        search_file_windows(filename, gui)

    elif intent == "brightness_up":
        brightness_up()
        speak("Increasing brightness")

    elif intent == "brightness_down":
        brightness_down()
        speak("Decreasing brightness")

    elif intent == "wifi_on":
        wifi_on()
        speak("Turning on WiFi")

    elif intent == "wifi_off":
        wifi_off()
        speak("Turning off WiFi")
        

    elif intent == "unknown":
        gui.status.setText("Sorry, I didn't understand that command.")
        speak("Sorry, I didn't understand that command.")