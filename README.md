# CodSoft Task No. 1 - Rule-Based Chatbot

This project is a simple rule-based chatbot built with Python, Flask, HTML, CSS, and JavaScript. The chatbot responds to user queries based on predefined rules and provides an introduction to natural language processing and basic conversation flow.

## Project Structure

codsoft_taskno.1/
├── app.py # Flask application with rule-based chatbot logic
├── templates/
│ └── index.html # HTML file for the chatbot interface
├── static/
│ ├── style.css # CSS file for styling the chatbot interface
│ └── script.js # JavaScript file for handling user interaction
├── .gitignore # Git ignore file
└── README.md # Project documentation file

````

### Files Explained

- **app.py**: The main server-side file that initializes the Flask app and contains the chatbot logic.
- **templates/index.html**: The frontend HTML file for displaying the chatbot interface to the user.
- **static/style.css**: The CSS file for styling the chatbot’s appearance.
- **static/script.js**: JavaScript file to manage user interactions with the chatbot.
- **README.md**: Project documentation and setup instructions.
- **.gitignore**: Specifies files and directories that Git should ignore.

## Features

- Rule-based responses based on keywords such as "hello", "bye", "how are you", and more.
- A dropdown selection for user inputs to make interaction easy.
- Simple UI with a chatbox, user input dropdown, and a send button.

## Requirements

- Python 3.x
- Flask
````
## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SocialisticO4/codsoft_taskno.1.git
   cd codsoft_taskno.1


2. **Install Dependencies**:
   Install Flask by running:

   ```bash
   pip install flask
   ```

3. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```
   The app will be accessible at `http://127.0.0.1:5000` in your web browser.

## Usage

1. **Select a Query**: From the dropdown menu, select a question or query.
2. **Click Send**: Click the send button to communicate with the chatbot.
3. **View Response**: The chatbot will reply in the chatbox with an appropriate response based on predefined rules.

## Adding More Responses

To add additional responses, modify the `get_bot_response` function in `app.py` by adding new entries to the `responses` dictionary. For example:

```python
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "goodbye": "Goodbye! Feel free to chat with me anytime.",
    # Add more responses here
}
```

## Technologies Used

- **Python** (Flask for backend)
- **HTML, CSS, JavaScript** (for the frontend interface)
- **GitHub** (for version control and code hosting)
