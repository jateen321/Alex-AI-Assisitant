
import datetime

class Logger:
    def __init__(self, log_file="assistant.log"):
        self.log_file = log_file
    def log(self, message, level='INFO'):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] [{level}] {message}\n"
        with open(self.log_file, 'a') as f:
          f.write(log_message)
        print(log_message, end="")

if __name__ == '__main__':
    logger = Logger()
    logger.log("This is an error message", level="error")
    logger.log("This is a test message", level="info")