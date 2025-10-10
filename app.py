from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os, json
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

CONTEXT_PROMPT = "אתה עוזר אישי שמדבר בעברית. השב בקצרה ובנימוס."
WELCOME_MESSAGE = "שלום! אני כאן כדי לעזור לך."
HISTORY_FILE = "history.json"

# --- Load history ---
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        all_chats = json.load(f)
else:
    all_chats = []

# --- Chat counter for unique names ---
CHAT_COUNTER = max([int(chat["name"].split("#")[1]) for chat in all_chats], default=0)

app = Flask(__name__)
CORS(app)

def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chats, f, ensure_ascii=False, indent=2)

@app.route("/chats", methods=["GET"])
def get_chats():
    return jsonify(all_chats)

@app.route("/chats/new", methods=["POST"])
def new_chat():
    global CHAT_COUNTER
    CHAT_COUNTER += 1
    chat_name = f"שיחה #{CHAT_COUNTER}"
    new_entry = {
        "name": chat_name,
        "messages": [
            {"role":"assistant","content":WELCOME_MESSAGE}
        ]
    }
    all_chats.append(new_entry)
    save_history()
    return jsonify(new_entry)

@app.route("/chats/<int:index>/send", methods=["POST"])
def send_message(index):
    if 0 <= index < len(all_chats):
        data = request.json
        user_input = data.get("message", "").strip()
        if not user_input:
            return jsonify({"error": "No message"}), 400

        all_chats[index]["messages"].append({"role":"user","content":user_input})

        try:
            resp = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role":"system","content":CONTEXT_PROMPT}] + all_chats[index]["messages"],
                max_tokens=500
            )
            bot_reply = resp.choices[0].message.content
        except Exception as e:
            bot_reply = f"[ERROR] {str(e)}"

        all_chats[index]["messages"].append({"role":"assistant","content":bot_reply})
        save_history()
        return jsonify({"reply": bot_reply})
    return jsonify({"error": "Invalid chat index"}), 400

@app.route("/chats/<int:index>/delete", methods=["POST"])
def delete_chat(index):
    if 0 <= index < len(all_chats):
        all_chats.pop(index)
        save_history()
        return jsonify({"status": "ok"})
    return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    app.run(debug=True)
