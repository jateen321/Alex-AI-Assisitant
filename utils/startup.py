
import os
import winreg
import sys
from pathlib import Path
from utils.logger import Logger

class StartupManager:
    def __init__(self, app_path, logger:Logger):
      self.app_path = app_path
      self.logger = logger
      self.registry_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

    def is_startup_enabled(self):
       """Checks if the application is set to run at startup."""
       try:
         key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_key)
         value, _ = winreg.QueryValueEx(key, "ai_assistant")
         winreg.CloseKey(key)
         return Path(value) == Path(self.app_path)
       except FileNotFoundError:
         return False

    def enable_startup(self):
        """Sets the application to run at startup."""
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_key, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "ai_assistant", 0, winreg.REG_SZ, str(self.app_path))
            winreg.CloseKey(key)
            self.logger.log("Startup enabled.")
            return True
        except Exception as e:
           self.logger.log(f"Failed to set Startup: {e}", level="error")
           return False

    def disable_startup(self):
      """Removes the application from running at startup."""
      try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_key, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, "ai_assistant")
        winreg.CloseKey(key)
        self.logger.log("Startup disabled.")
        return True
      except FileNotFoundError:
            self.logger.log("Startup entry not found, nothing to disable.", level="info")
            return True
      except Exception as e:
            self.logger.log(f"Failed to disable Startup: {e}", level="error")
            return False

if __name__ == '__main__':
    logger = Logger()
    app_path = sys.executable
    startup = StartupManager(app_path, logger)
    if startup.is_startup_enabled():
       print("Startup enabled.")
    else:
        print("Startup disabled.")
    if startup.enable_startup():
       print("Startup Enabled.")
    else:
        print("Startup failed")

    if startup.disable_startup():
      print("Startup Disabled.")
    else:
        print("Startup failed")
    if startup.is_startup_enabled():
       print("Startup enabled.")
    else:
        print("Startup disabled.")