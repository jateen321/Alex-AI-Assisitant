
# AI Assistant

This is an AI Assistant application designed to help users interact with their computer through voice and text commands.

## Features

- **Voice and Text Command Execution:** Opens files, folders, and applications based on user voice or text.
- **Gemini Integration:** Chats with users using Google Gemini.
- **Startup Functionality:** Optionally starts the application at login.
- **User Interface:** A user friendly text interface
- **Logging** Logs application events to a local file for debug purposes
- **Config Management** Handles api keys and default application configuration
- **System Monitoring** displays CPU and Memory utilization for better user experince

## Getting Started

1.  **Clone the repository:**
content_copy
download
Use code with caution.
Markdown

git clone https://your_github_repo/your_repo_name.git

2.  **Navigate to the project directory:**
    
   cd your_repo_name
    

3.  **Create a virtual environment:**
  bash
    python -m venv venv
    

4. **Activate the virtual environment:**
  bash
   venv\Scripts\activate #On Windows
content_copy
download
Use code with caution.

Install dependencies:

pip install -r requirements.txt
content_copy
download
Use code with caution.

Run the application:

python main.py
    ```
*Configuration*:

1. Create a Google Gemini API key through Google AI Studio.
2. Replace "Enter_API_Key" with your Gemini API Key in the  user_config.json file under the data/ folder
3. The program creates a user_config.json file in the data directory if it does not exist.
4. Modify app_paths section in data/user_config.json to your desired application executable path.

## TODO
*  Refactor all functions and modules for better modularity and clean code
*   Add proper unit tests for each module.
* Add More error handling for user input, and invalid