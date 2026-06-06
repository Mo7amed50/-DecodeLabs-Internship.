"""Flask web UI for the DecodeLabs rule-based chatbot."""

from flask import Flask, render_template, request, jsonify

from chatbot import normalize
from responses import EXIT_SENTINEL, get_response

app = Flask(__name__)

WELCOME_MESSAGE = (
    "DecodeLabs Project 1: Rule-Based Bot\n"
    "Batch 2026\n\n"
    "Type a message below and hit Send. Use 'bye' to exit."
)


@app.route("/")
def index():
    return render_template("index.html", welcome=WELCOME_MESSAGE)


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()
    if not user_message:
        return jsonify(
            reply="Please type something, or 'bye' to exit.",
            exit=False,
        )

    text = normalize(user_message)
    reply = get_response(text)
    should_exit = reply == EXIT_SENTINEL
    return jsonify(
        reply=(
            "Goodbye! Thanks for chatting. See you at DecodeLabs."
            if should_exit
            else reply
        ),
        exit=should_exit,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
