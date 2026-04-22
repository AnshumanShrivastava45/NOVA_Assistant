import sys
from PyQt6.QtWidgets import QApplication

from gui.main_window import AssistantGUI
from core.wake_word import detect_wake_word
from features.face_auth import authenticate_face


def main():

    print("Assistant is sleeping...")

    while True:

        if detect_wake_word():

            print("Wake word detected!")

            if not authenticate_face():
                 print("Access Denied")
                 continue
            
            print("Access Granted")

            app = QApplication(sys.argv)

            window = AssistantGUI()
            window.show()

            sys.exit(app.exec())


if __name__ == "__main__":
    main()