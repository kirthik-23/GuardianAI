import json
import guardian
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = "guardian_secret_key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data["message"]
    if "history" not in session:
        session["history"] = []
    history = session["history"]
    history.append("User: " + user_message)
    print("User message:",user_message)
    reply = guardian.ask_guardian(user_message)
    history.append("Guardian: " + reply)
    session["history"] = history
    return jsonify({
         "reply": reply
    })
@app.route("/memory")
def memory():

    try:

        with open("memory.json", "r", encoding="utf-8") as f:

            data = json.load(f)

    except:

        data = {}

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
