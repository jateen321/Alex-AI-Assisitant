
import speech_recognition as sr
from utils.logger import Logger

class SpeechHandler:
    def __init__(self, logger : Logger):
       self.recognizer = sr.Recognizer()
       self.logger = logger
    def listen(self):
        """Listens for voice input and returns the recognized text."""
        with sr.Microphone() as source:
            self.logger.log("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
              audio = self.recognizer.listen(source, timeout=5)
            except sr.WaitTimeoutError:
              self.logger.log("Listening timed out", level='error')
              return "" # Handle Timeout
        try:
             text = self.recognizer.recognize_google(audio)
             self.logger.log(f"You said: {text}")
             return text
        except sr.UnknownValueError:
            self.logger.log("Could not understand audio", level='error')
            return ""
        except sr.RequestError as e:
            self.logger.log(f"Error fetching recognition service; {e}", level='error')
            return ""


if __name__ == '__main__':
    logger = Logger()
    speech_handler = SpeechHandler(logger)
    while True:
      voice = speech_handler.listen()
      if voice:
         print("You Said: ", voice)