
import sys
import time
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from utils.startup import StartupManager
from utils.logger import Logger
from core.config import Config
from core.app_manager import AppManager
from core.gemini_handler import GeminiHandler
from core.command_handler import CommandHandler
from utils.system import SystemUtils

def main():
    app = QApplication(sys.argv)
    logger = Logger()
    config = Config()
    system_utils = SystemUtils()
    app_manager = AppManager(logger, config)
    gemini_handler = GeminiHandler(logger, config)
    command_handler = CommandHandler(logger, app_manager, gemini_handler)
    startup_manager = StartupManager(sys.executable, logger) # Get Current Path

    if not startup_manager.is_startup_enabled():
       #Enable for testing only, Remove for real builds.
       startup_manager.enable_startup()
       #Disable for testing only, Remove for real builds.
       #startup_manager.disable_startup()

    main_window = MainWindow(logger, command_handler, config, system_utils, sys.executable)
    main_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
   main()