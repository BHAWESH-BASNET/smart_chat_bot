from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os, json
from openai import OpenAI

# --- טעינת משתני סביבה ---
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

# --- קבועים ---
CONTEXT_PROMPT = "אתה עוזר אישי שמדבר בעברית. השב בקצרה ובנימוס."
WELCOME_MESSAGE = "שלום! אני כאן כדי לעזור לך."
HISTORY_FILE = "history.json"

# --- טעינת היסטוריית שיחות ---
try:
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        all_chats = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    all_chats = []

# --- מונה שיחות ---
CHAT_COUNTER = max(
    [int(chat["name"].split("#")[1]) for chat in all_chats if "#" in chat["name"]],
    default=0
)

# --- הגדרת Flask ---
app = Flask(__name__)
CORS(app)

def save_history():
    """שמירת כל ההיסטוריה לקובץ"""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chats, f, ensure_ascii=False, indent=2)

# --- קבלת כל השיחות ---
@app.route("/chats", methods=["GET"])
def get_chats():
    return jsonify(all_chats)

# --- יצירת שיחה חדשה ---
@app.route("/chats/new", methods=["POST"])
def new_chat():
    global CHAT_COUNTER
    CHAT_COUNTER += 1
    chat_name = f"שיחה #{CHAT_COUNTER}"
    new_entry = {
        "name": chat_name,
        "messages": [
            {"role": "assistant", "content": WELCOME_MESSAGE}
        ]
    }
    all_chats.append(new_entry)
    save_history()
    return jsonify(new_entry)

# --- שליחת הודעה ---
@app.route("/chats/<int:index>/send", methods=["POST"])
def send_message(index):
    if not (0 <= index < len(all_chats)):
        return jsonify({"error": "Invalid chat index"}), 400

    data = request.json
    user_input = data.get("message", "").strip()
    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    all_chats[index]["messages"].append({"role": "user", "content": user_input})

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": CONTEXT_PROMPT}] + all_chats[index]["messages"],
            max_tokens=500
        )
        bot_reply = resp.choices[0].message.content
    except Exception as e:
        bot_reply = f"[שגיאה] {str(e)}"

    all_chats[index]["messages"].append({"role": "assistant", "content": bot_reply})
    save_history()
    return jsonify({"reply": bot_reply})

# --- מחיקת שיחה ---
@app.route("/chats/<int:index>/delete", methods=["POST"])
def delete_chat(index):
    if 0 <= index < len(all_chats):
        all_chats.pop(index)
        save_history()
        return jsonify({"status": "ok", "chats": all_chats})
    return jsonify({"status": "error"}), 400

# --- הפעלת השרת ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
