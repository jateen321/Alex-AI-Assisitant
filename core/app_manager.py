import os
import subprocess
import webbrowser
from utils.logger import Logger
from pathlib import Path
from core.config import Config

class AppManager:
    def __init__(self, logger:Logger, config: Config):
      self.logger = logger
      self.config = config
      self.paths = self.config.app_paths

    def open_file(self, file_path):
        """Opens a file using the default application."""
        try:
            if not Path(file_path).exists():
              self.logger.log(f"File {file_path} not found!", level="error")
              return False
            os.startfile(file_path)
            self.logger.log(f"Opened file: {file_path}")
            return True
        except Exception as e:
            self.logger.log(f"Error opening file: {e}", level='error')
            return False

    def open_folder(self, folder_path):
        """Opens a folder in file explorer."""
        try:
            if not Path(folder_path).exists():
                self.logger.log(f"File {folder_path} not found!", level="error")
                return False
            os.startfile(folder_path)
            self.logger.log(f"Opened folder: {folder_path}")
            return True
        except Exception as e:
            self.logger.log(f"Error opening folder: {e}", level='error')
            return False

    def open_app(self, app_name):
        """Opens an application based on its name or a provided executable path."""
        app_path = self.config.get_app_path(app_name)
        if not app_path:
          self.logger.log(f"Cannot locate {app_name}, please configure in user_config.json", level="error")
          return False
        try:
            subprocess.Popen([app_path])
            self.logger.log(f"Opened App: {app_name}")
            return True
        except Exception as e:
            self.logger.log(f"Error opening application: {e}", level='error')
            return False

    def open_url(self, url):
      try:
            webbrowser.open(url)
            self.logger.log(f"Opened Website: {url}")
            return True
      except Exception as e:
            self.logger.log(f"Error opening website: {e}", level='error')
            return False



    def find_executable(self, app_name):
         """This function searches all of your local drives and find executable files."""
         try:
             for drive_letter in [chr(i) + ":" for i in range(65, 91)]:  # A-Z Drives
                app_path = self._search_directory(drive_letter + "/", app_name+".exe")
                if app_path:
                    return app_path
         except Exception as e:
             self.logger.log(f"Unable to search local drives {e}", level='error')
             return None
         return None
    def _search_directory(self, dir_path, filename):
        """Helper Function"""
        try:
          for root, dirs, files in os.walk(dir_path):
              if filename in files:
                  return os.path.join(root, filename)
          return None
        except Exception as e:
            self.logger.log(f"Unable to search directory {dir_path} with error {e}", level="error")
            return None



if __name__ == '__main__':
    logger = Logger()
    config = Config()
    app_manager = AppManager(logger, config)
    app_manager.open_url("https://google.com")
    app_manager.open_file(r"c:\users\Public\Documents\sample.txt")
    app_manager.open_folder(r"c:\users\Public\Documents")
    app_manager.open_app("code")
    executable_path = app_manager.find_executable("notepad")
    if executable_path:
        print("Executable Path ", executable_path)