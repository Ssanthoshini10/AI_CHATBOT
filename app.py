from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>AI Chatbot</h2>
    <form action="/chat">
        <input type="text" name="msg" placeholder="Type a message">
        <input type="submit" value="Send">
    </form>
    """

@app.route("/chat")
def chat():
    msg = request.args.get("msg")

    if msg and msg.lower() == "hello":
        return "Hi! How are you?"
    elif msg and msg.lower() == "how are you":
        return "I am fine."
    else:
        return "Sorry, I don't understand."

if __name__ == "__main__":
    app.run(debug=True)