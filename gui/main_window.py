import sys
from pathlib import Path
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QTextEdit, QLineEdit, QLabel, QPushButton, QDialog, QScrollArea)
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QIcon, QMovie, QPixmap, QPalette, QColor, QBrush
from gui.style import chat_style, input_box_style, button_style, label_style, main_window_style, icon_style, message_box_style
from core.speech_handler import SpeechHandler
from core.command_handler import CommandHandler
from utils.system import SystemUtils
from utils.logger import Logger
from core.config import Config

class SettingsDialog(QDialog):
    def __init__(self, config: Config, parent=None):
        super().__init__(parent)
        self.config = config
        self.setWindowTitle("Settings")
        layout = QVBoxLayout(self)

        self.gemini_key_label = QLabel("Gemini API Key:")
        self.gemini_key_input = QLineEdit()
        self.gemini_key_input.setText(self.config.get_gemini_key())
        layout.addWidget(self.gemini_key_label)
        layout.addWidget(self.gemini_key_input)

        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet(button_style)
        self.save_button.clicked.connect(self.save_settings)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_settings(self):
        new_gemini_api_key = self.gemini_key_input.text()
        if new_gemini_api_key:
            self.config.update_gemini_key(new_gemini_api_key)
        self.close()

class MainWindow(QWidget):
    def __init__(self, logger: Logger, command_handler: CommandHandler, config: Config, system_utils: SystemUtils, app_path: str):
        super().__init__()
        self.app_path = app_path
        self.logger = logger
        self.config = config
        self.command_handler = command_handler
        self.system_utils = system_utils
        self.speech_handler = SpeechHandler(logger)
        self.setWindowTitle("Alex Prajapathy")
        self.setWindowIcon(QIcon(str(Path("gui/assets/animated_icon.gif"))))

        self.setStyleSheet(main_window_style)

        # Set background image
        self.setAutoFillBackground(True)
        palette = self.palette()
        background_image_path = Path("gui/assets/background.png")
        if background_image_path.exists():
            background_image = QPixmap(str(background_image_path))
            background_image = background_image.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
            palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        else:
            self.logger.log(f"Background image not found at {background_image_path}", level="error")
        self.setPalette(palette)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icon_layout = QHBoxLayout()
        icon_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.icon_label = QLabel()
        self.icon_label.setStyleSheet(icon_style)
        self.icon_label.setFixedSize(100, 100)
        self.icon_movie = QMovie(str(Path("gui/assets/animated_icon.gif")))
        self.icon_label.setMovie(self.icon_movie)
        self.icon_movie.start()
        icon_layout.addWidget(self.icon_label)

        main_layout.addLayout(icon_layout)

        self.chat_display = QScrollArea()
        self.chat_display.setWidgetResizable(True)
        self.chat_display_widget = QWidget()
        self.chat_display_layout = QVBoxLayout(self.chat_display_widget)
        self.chat_display.setWidget(self.chat_display_widget)
        main_layout.addWidget(self.chat_display)

        input_layout = QHBoxLayout()

        self.input_box = QLineEdit()
        self.input_box.setStyleSheet(input_box_style)
        input_layout.addWidget(self.input_box)

        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet(button_style)
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)

        self.speech_button = QPushButton("🎤")
        self.speech_button.setStyleSheet(button_style)
        self.speech_button.clicked.connect(self.speech_input)
        input_layout.addWidget(self.speech_button)

        main_layout.addLayout(input_layout)

        self.setLayout(main_layout)

    def send_message(self):
        message = self.input_box.text()
        self.add_message(f"You: {message}", align_right=True)
        response = self.command_handler.process(message)
        self.add_message(f"Assistant: {response}", align_right=False)
        self.input_box.clear()

    def speech_input(self):
        self.add_message("Listening...", align_right=True)
        message = self.speech_handler.listen()
        self.input_box.setText(message)
        self.add_message(f"You: {message}", align_right=True)
        response = self.command_handler.process(message)
        self.add_message(f"Assistant: {response}", align_right=False)

    def add_message(self, text, align_right=False):
        message_label = QLabel(text)
        message_label.setStyleSheet(message_box_style)
        message_label.setWordWrap(True)  # Enable word wrap
        message_layout = QHBoxLayout()
        if align_right:
            message_layout.addStretch()
            message_layout.addWidget(message_label)
        else:
            message_layout.addWidget(message_label)
            message_layout.addStretch()
        self.chat_display_layout.addLayout(message_layout)
        self.chat_display.verticalScrollBar().setValue(self.chat_display.verticalScrollBar().maximum())

    def open_settings(self):
        settings_dialog = SettingsDialog(self.config, self)
        settings_dialog.exec()

    def update_resource_label(self):
        cpu_usage = self.system_utils.get_cpu_usage()
        memory_usage = self.system_utils.get_memory_usage()
        self.add_message(f"CPU Usage: {cpu_usage}%", align_right=False)
        self.add_message(f"Memory Usage: {memory_usage}%", align_right=False)

if __name__ == '__main__':
    logger = Logger()
    config = Config()
    system_utils = SystemUtils()
    from core.app_manager import AppManager
    app_manager = AppManager(logger, config)
    from core.gemini_handler import GeminiHandler
    gemini_handler = GeminiHandler(logger, config)
    from core.command_handler import CommandHandler
    command_handler = CommandHandler(logger, app_manager, gemini_handler)

    app = QApplication(sys.argv)
    main_window = MainWindow(logger, command_handler, config, system_utils, sys.executable)
    main_window.show()
    sys.exit(app.exec())