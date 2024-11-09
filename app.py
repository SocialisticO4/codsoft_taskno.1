from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Rule-based chatbot logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # Predefined responses
    responses = {
        "hello": "Hello! How can I assist you today?",
        "how are you": "I'm just a bot, but thanks for asking! How can I help?",
        "what is your name": "I'm ChatBot, your assistant!",
        "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "bye": "Goodbye! Feel free to chat with me anytime.",
        "what can you do": "I can answer questions, tell jokes, and assist with basic inquiries. Just select an option!"
    }

    # Return a response based on the input or a default message if input is not recognized
    return responses.get(user_input, "I'm sorry, I don't understand that. Try asking something else.")

# Route for the chatbot
@app.route("/")
def index():
    return render_template("index.html")

# Endpoint to handle user messages
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
