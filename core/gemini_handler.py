import google.generativeai as genai
from core.config import Config
from utils.logger import Logger

class GeminiHandler:
    def __init__(self, logger:Logger, config: Config):
       self.logger = logger
       self.config = config
       self.api_key = self.config.get_gemini_key()
       if not self.api_key or self.api_key == "Enter_API_Key":
          self.logger.log("Please configure api key in the user_config.json", level="error")
          exit()
       genai.configure(api_key = self.api_key)
       self.model = genai.GenerativeModel('gemini-1.5-flash')


    def chat(self, prompt):
      try:
        response = self.model.generate_content("You are a chill guy who is slightly sarcastic and humorous addressing me as sir. you are named Alex Prajapathy but you go by the Alex. You always give to the point helpful answers. You can open Sotify, google, news, VSCode, google classroom, linkedin and Genship Impact."+prompt)
        if response and response.text:
            self.logger.log(f"Alex Response: {response.text}")
            return response.text
        else:
            self.logger.log(f"Alex is busyy", level="error")
            return None
      except Exception as e:
        self.logger.log(f"Error accessing Alex : {e}", level="error")
        return None

if __name__ == '__main__':
  logger = Logger()
  config = Config()
  gemini_handler = GeminiHandler(logger, config)
  while True:
    prompt = input("Enter text for Alex or 'exit' to end: ")
    if prompt.lower() == 'exit':
        break
    response = gemini_handler.chat(prompt)
    if response:
      print("Response: ", response)
