
import json
import os
from pathlib import Path

class Config:
    def __init__(self, config_file="data/user_config.json"):
        self.config_file = Path(config_file)
        self.data = self._load_config()
        self.gemini_api_key = self.data.get("gemini_api_key")
        self.app_paths = self.data.get("app_paths")

    def _load_config(self):
         if not os.path.exists(self.config_file):
            print("Creating config file")
            initial_data = {
                "gemini_api_key": "AIzaSyBEzjqJl7y7zyY2S_yy2vivqhj-_7-SNpE",
                "app_paths": {
                    "music": r"C:\Users\athar\AppData\Roaming\Spotify\Spotify.exe",
                    "news": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    "code": r"C:\Users\athar\AppData\Local\Programs\Microsoft VS Code\Code.exe",
                    "game": r"C:\Program Files\HoYoPlay\launcher.exe"
                }
            }
            with open(self.config_file, 'w') as f:
                json.dump(initial_data, f, indent=4)
            return initial_data
         else:
            try:
               with open(self.config_file, 'r') as f:
                   return json.load(f)
            except Exception as e:
              print("Error loading config file", e)
              return {}


    def save_config(self):
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            print(f"Failed to save configuration: {e}")


    def add_app_path(self, app_name, app_path):
       if self.app_paths is None:
           self.app_paths = {}
       self.app_paths[app_name] = app_path
       self.data["app_paths"] = self.app_paths
       self.save_config()

    def get_app_path(self,app_name):
         if self.app_paths and app_name in self.app_paths:
           return self.app_paths.get(app_name)
         return None

    def update_gemini_key(self, gemini_api_key):
        self.gemini_api_key = gemini_api_key
        self.data["gemini_api_key"] = gemini_api_key
        self.save_config()

    def get_gemini_key(self):
        return self.gemini_api_key

    def update_data(self, key, value):
        self.data[key] = value
        self.save_config()

    def get_data(self, key):
        if key in self.data:
            return self.data[key]
        return None

if __name__ == '__main__':
    config = Config()
    print(config.data)