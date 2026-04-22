from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QPen

from core.speech_engine import take_command
from core.intent_classifier import predict_intent
from core.command_router import execute_intent
import threading
from core.assistant_engine import start_assistant


class AnimatedCircle(QWidget):

    def __init__(self):
        super().__init__()

        self.radius = 50
        self.growing = True
        
        self.setMinimumSize(200, 200)

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(50)

    def animate(self):

        if self.growing:
            self.radius += 2
            if self.radius > 70:
                self.growing = False
        else:
            self.radius -= 2
            if self.radius < 50:
                self.growing = True

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen(QColor(0, 255, 255))
        pen.setWidth(4)

        painter.setPen(pen)

        center_x = self.width() // 2
        center_y = self.height() // 2

        painter.drawEllipse(
            center_x - self.radius,
            center_y - self.radius,
            self.radius * 2,
            self.radius * 2
            )


class AssistantGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NOVA Assistant")
        self.setGeometry(500, 200, 400, 500)

        self.title = QLabel("NOVA")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.circle = AnimatedCircle()

        self.status = QLabel("Assistant Ready")
        self.status.setWordWrap(True)
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status.setMaximumWidth(350)

        #self.system_btn = QPushButton("System Mode")
        #self.ai_btn = QPushButton("AI Mode")
        self.system_label = QLabel("System Mode")
        self.ai_label = QLabel("AI Mode")

        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.circle)
        layout.addWidget(self.status)
        layout.addWidget(self.system_label)
        layout.addWidget(self.ai_label)

        self.setLayout(layout)

        # self.system_btn.clicked.connect(self.listen_command)
        threading.Thread(target=start_assistant, args=(self,), daemon=True).start()

"""    def listen_command(self):

        self.status.setText("Listening...")

        command = take_command()

        if command != "":

            intent = predict_intent(command)

            #self.status.setText(f"Intent: {intent}")

            execute_intent(intent, command)

        else:

            self.status.setText("Could not understand")

"""








"""
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from core.speech_engine import take_command
from core.intent_classifier import predict_intent
from core.command_router import execute_intent

class AssistantGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voice Assistant")
        self.setGeometry(500, 200, 400, 500)

        self.label = QLabel("Assistant Sleeping...")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.system_btn = QPushButton("System Mode")
        self.ai_btn = QPushButton("AI Mode")

        layout = QVBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.system_btn)
        layout.addWidget(self.ai_btn)

        self.setLayout(layout)

        # button actions
        self.system_btn.clicked.connect(self.listen_command)

    def listen_command(self):

        self.label.setText("Listening...")

        command = take_command()

        if command != "":
            intent = predict_intent(command)
            self.label.setText(f"Intent: {intent}")
            self.label.setText(f"Command: {command}")
            execute_intent(intent,command)
        else:
            self.label.setText("Could not understand")
"""