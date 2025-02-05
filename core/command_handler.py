from core.app_manager import AppManager
from core.gemini_handler import GeminiHandler
from utils.logger import Logger

class CommandHandler:
    def __init__(self, logger: Logger, app_manager: AppManager, gemini_handler: GeminiHandler):
        self.logger = logger
        self.app_manager = app_manager
        self.gemini_handler = gemini_handler
        self.actions = {
            "music": self._play_music,
            "whats going on": self._whats_going_on,
            "code": self._lets_code,
            "game": self._lets_play,
            "assignment": self._open_classroom,
            "assignments": self._open_classroom,
            "work left": self._open_classroom,
            "classroom": self._open_classroom,
            "job": self._open_linkedin,
            "placement": self._open_linkedin,
            "linkedin": self._open_linkedin
        }

    def process(self, command):
        command = command.lower().strip()
        self.logger.log(f"Command to Process: {command}")

        if command.startswith("tell me"):
            prompt = command.replace("tell me", "").strip()
            return self.gemini_handler.chat(prompt)

        for keyword, action in self.actions.items():
            if keyword in command:
                return action()

        return f"I don't know what {command} means"

    def _play_music(self):
        if self.app_manager.open_app("music"):
            return "Playing Music"
        return "Unable to Open Music"

    def _whats_going_on(self):
        if self.app_manager.open_url("https://www.bbc.com/news"):
            return "Opening BBC News"
        return "Unable to open Website"

    def _lets_code(self):
        if self.app_manager.open_app("code"):
            return "Opening Visual Studio Code"
        return "Unable to open VSCode"

    def _lets_play(self):
        if self.app_manager.open_app("game"):
            return "Opening Game"
        return "Unable to open Game"

    def _open_classroom(self):
        if self.app_manager.open_url("https://classroom.google.com/a/not-turned-in"):
            return "Opening Google Classroom"
        return "Unable to open Google Classroom"

    def _open_linkedin(self):
        if self.app_manager.open_url("https://linkedin.com/feed/"):
            return "Opening LinkedIn"
        return "Unable to open LinkedIn"

if __name__ == '__main__':
    logger = Logger()
    from core.config import Config
    config = Config()
    app_manager = AppManager(logger, config)
    gemini_handler = GeminiHandler(logger, config)
    command_handler = CommandHandler(logger, app_manager, gemini_handler)
    while True:
        command = input("Enter command or exit to end: ")
        if command.lower() == "exit":
            break
        response = command_handler.process(command)
        if response:
            print("Response: ", response)