import ctypes
from datetime import datetime
from os import path
import os
import pyautogui
import time
import webbrowser
import subprocess
import screen_brightness_control as sbc
import json

FILE = "memory.json"

apps = {
    "chrome": r"C:\Users\hp\AppData\Local\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "vs code": r"C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}


def open_application(app_name):

    app_name = app_name.lower()

    if app_name in apps:
        try:
            os.startfile(apps[app_name])
            print(f"Opening {app_name}")

        except Exception as e:
            print("Error opening app:", e)
    else:
        print("Application not found")


def shutdown_pc():
    os.system("shutdown /s /t 1")


def restart_pc():
    os.system("shutdown /r /t 1")

def brightness_up():
    sbc.set_brightness('+10')

def brightness_down():
    sbc.set_brightness('-10')

def wifi_on():
    os.system("netsh interface set interface Wi-Fi enabled")

def wifi_off():
    os.system("netsh interface set interface Wi-Fi disabled")
    

def take_screenshot():

    folder_path = "screenshots"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshot_{timestamp}.png"

    full_path = os.path.join(folder_path, file_name)

    screenshot = pyautogui.screenshot()
    screenshot.save(full_path)

    print(f"Screenshot saved: {full_path}")
    
def open_folder(command, gui=None):

    command = command.lower()

    home = os.path.expanduser("~")

    folders = {
        "download": os.path.join(home, "Downloads"),
        "downloads": os.path.join(home, "Downloads"),

        "document": os.path.join(home, "Documents"),
        "documents": os.path.join(home, "Documents"),

        "desktop": os.path.join(home, "Desktop"),

        "picture": os.path.join(home, "Pictures"),
        "pictures": os.path.join(home, "Pictures"),
    }

    for key in folders:

        if key in command:

            path = folders[key]

            print("Opening path:", path)

            if os.path.exists(path):

                os.startfile(path)

                if gui:
                    gui.status.setText(f"Opening {key} folder")

                return

    if gui:
        gui.status.setText("Folder not found")

def lock_system():
    ctypes.windll.user32.LockWorkStation()

def volume_up():
    pyautogui.press("volumeup")

def volume_down():
    pyautogui.press("volumedown")

def mute():
    pyautogui.press("volumemute")

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def save_memory(text):
    data = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append(text)

    with open(FILE, "w") as f:
        json.dump(data, f)


def get_memory():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)
            return "\n".join(data)
    return "No memory found"

def search_file_windows(filename, gui=None):

    try:
        command = [
            "powershell",
            "-Command",
            f"Get-ChildItem -Path C:\\ -Recurse -ErrorAction SilentlyContinue | Where-Object {{$_.Name -like '*{filename}*'}} | Select-Object -First 1 -ExpandProperty FullName"
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        path = result.stdout.strip()

        if path and os.path.exists(path):

            if gui:
                gui.status.setText(f"Found: {os.path.basename(path)}")

            os.startfile(path)

            return path

        else:
            if gui:
                gui.status.setText("File not found")

    except Exception as e:

        if gui:
            gui.status.setText("Error searching file")

        print("Search error:", e)