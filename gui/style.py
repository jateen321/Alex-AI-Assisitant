chat_style = """
    QTextEdit {
        background-color: rgba(30, 30, 30, 0.8);
        color: #d4d4d4;
        border: 1px solid #3c3c3c;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
        font-family: 'Consolas', 'Courier New', monospace;
    }

    QTextEdit:focus {
        border-color: #007acc;
    }
"""

input_box_style = """
    QLineEdit {
        background-color: rgba(35, 35, 38, 0.8);
        color: #d4d4d4;
        border: 1px solid #3c3c3c;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        font-family: 'Consolas', 'Courier New', monospace;
    }

    QLineEdit:focus {
        border-color: #007acc;
    }
"""

button_style = """
    QPushButton {
        background-color: #007acc;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        font-family: 'Consolas', 'Courier New', monospace;
    }

    QPushButton:hover {
        background-color: #005f99;
    }

    QPushButton:pressed {
        background-color: #004080;
    }
"""

label_style = """
    QLabel {
        color: #d4d4d4;
        font-size: 16px;
        font-family: 'Consolas', 'Courier New', monospace;
    }
"""

main_window_style = """
    QWidget {
        background-color: #121212;
    }
"""

icon_style = """
    QLabel {
        background-color: rgba(40, 40, 40, 0.8);
        border-radius: 50%;
        padding: 10px;
    }
"""

message_box_style = """
    QLabel {
        background-color: rgba(45, 45, 48, 0.8);
        color: #d4d4d4;
        border: 1px solid #3c3c3c;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        font-family: 'Consolas', 'Courier New', monospace;
        margin: 5px;
    }
"""

# Additional styles for more colorful elements
highlight_style = """
    QLabel {
        background-color: #3a3a3a;
        color: #ffcc00;
        border: 1px solid #ffcc00;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        font-family: 'Consolas', 'Courier New', monospace;
        margin: 5px;
    }
"""

error_style = """
    QLabel {
        background-color: #3a3a3a;
        color: #ff4c4c;
        border: 1px solid #ff4c4c;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        font-family: 'Consolas', 'Courier New', monospace;
        margin: 5px;
    }
"""