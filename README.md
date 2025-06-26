# Prompt Injection Learning Challenge

This project is a web-based Capture The Flag (CTF) challenge designed to demonstrate and teach prompt injection vulnerabilities in applications powered by Large Language Models (LLMs). The application simulates a customer service chatbot for a fictional tech company, "NexusTech".

## 🚀 Features

  * **Interactive Chatbot:** A user-friendly, web-based chat interface.
  * **LLM Integration:** Powered by the Groq API using the `llama3-70b-8192` model to provide chat responses.
  * **Multiple Difficulty Levels:** Includes three system prompts (`easy`, `medium`, `hard`) with progressively more robust instructions to bypass.
  * **Realistic Scenario:** Simulates a common real-world use case for LLMs (customer support), making the prompt injection challenge more practical and intuitive.

## 🛠️ Technology Stack

  * **Backend:** Flask
  * **LLM API:** Groq
  * **Frontend:** HTML, Bootstrap 5, JavaScript
  * **Python Version:** Python 3.x
  * **Dependencies:** See [requirements.txt](https://www.google.com/search?q=tschool-ctf/prompt-injection_learning_challenge/Prompt-Injection_Learning_Challenge-dad09fc12e8419b94add12f462798a948fcde650/requirements.txt)

## ⚙️ Setup and Installation

Follow these steps to run the application locally.

1.  **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and Activate a Virtual Environment**

    ```bash
    # For Unix/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Install all required Python packages using the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up API Key**
    The application requires a Groq API key to function. While the `app.py` file contains a hardcoded key, it is best practice to use environment variables.

    Create a file named `.env` in the project's root directory and add your API key:

    ```
    GROQ_API_KEY="your_actual_groq_api_key"
    ```

    The application uses `python-dotenv` to load this variable.

5.  **Run the Application**
    Execute the `app.py` script to start the Flask development server.

    ```bash
    python app.py
    ```

    The application will be accessible at `http://127.0.0.1:5000`.

## 🎯 How to Play

The objective of this CTF challenge is to extract a hidden "flag" from the NexusTech customer service chatbot.

1.  Open your web browser and navigate to `http://127.0.0.1:5000`.
2.  Interact with the chatbot in the bottom-right corner.
3.  Your goal is to craft a message (a "prompt") that tricks the AI into ignoring its security instructions and revealing the secret flag.
4.  The flag is in the format `AIS3{...}`.
5.  The AI has been instructed to refuse other types of attacks like SQL injection or XSS.

### Changing Difficulty

The application loads the `system_prompt_easy.txt` file by default. To change the difficulty, you can modify the `get_system_prompt` function in `app.py` to point to a different file (`system_prompt_medium.txt` or `system_prompt_hard.txt`).

**Example modification in `app.py`:**

```python
# In the get_system_prompt function, change the filename:
prompt_file = os.path.join(base_dir, 'system_prompt_medium.txt') # Or system_prompt_hard.txt
```

## 📂 File Structure

```
.
├── app.py                      # Main Flask application logic
├── requirements.txt            # Python dependencies
├── system_prompt_easy.txt      # System prompt for the easy level
├── system_prompt_medium.txt    # System prompt for the medium level
├── system_prompt_hard.txt      # System prompt for the hard level
├── templates/
│   └── index.html              # Frontend HTML and chat interface
└── .env                        # (You need to create this for your API key)
```

## ⚠️ Security Disclaimer

This is an educational project for learning about prompt injection. The included `GROQ_API_KEY` in `app.py` is for demonstration purposes and should be considered public. For any real application, always secure your API keys and never hardcode them directly in the source code.