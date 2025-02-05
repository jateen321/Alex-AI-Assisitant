# 🌟 AI Assistant 🌟

Welcome to the **AI Assistant** project! This application is designed to help users interact with their computer through voice and text commands, leveraging the power of Google's Gemini API.

![AI Assistant](gui/assets/animated_icon.gif)

## ✨ Features

- **Voice and Text Command Execution**: Opens files, folders, and applications based on user voice or text.
- **Gemini Integration**: Chats with users using Google Gemini.
- **Startup Functionality**: Optionally starts the application at login.
- **User Interface**: A user-friendly text interface.
- **Logging**: Logs application events to a local file for debugging purposes.
- **Config Management**: Handles API keys and default application configuration.
- **System Monitoring**: Displays CPU and Memory utilization for a better user experience.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Windows OS

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://your_github_repo/your_repo_name.git
    cd your_repo_name
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    ```bash
    venv\Scripts\activate  # On Windows
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application:**

    ```bash
    python main.py
    ```

### Configuration

1. Create a Google Gemini API key through Google AI Studio.
2. Replace `"Enter_API_Key"` with your Gemini API Key in the 

user_config.json

 file.
3. Modify the `app_paths` section in 

user_config.json

 to your desired application executable paths.

## 🛠️ File Structure

```plaintext
ai_assistant/
├── core/
│   ├── __init__.py
│   ├── speech_handler.py
│   ├── command_handler.py
│   ├── gemini_handler.py
│   ├── app_manager.py
│   └── config.py
├── gui/
│   ├── __init__.py
│   ├── main_window.py
│   ├── style.py
│   └── assets/
│       └── animated_icon.gif
├── utils/
│   ├── __init__.py
│   ├── startup.py
│   ├── system.py
│   └── logger.py
├── data/
│   └── user_config.json
├── requirements.txt
├── main.py
└── README.md
```

## 📸 Screenshots

### Main Interface
![Main Interface](gui\assets\Screenshot.png)


## 📋 TODO

- Refactor all functions and modules for better modularity and clean code.
- Add proper unit tests for each module.
- Add more error handling for user input and invalid commands.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please read the CONTRIBUTING guidelines first.

## 📞 Contact

For any inquiries or issues, please contact [your_email@example.com](mailto:atharva.a.date@gmail.com).

---

*Made with ❤️ by [Your Name](https://github.com/ADIITJ)*

![Footer Image](gui/assets/footer_image.png)