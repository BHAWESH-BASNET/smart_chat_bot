<div dir="rtl">

  <h1>🤖 SmartChat — Secure Hebrew Chatbot</h1>

  <p>
    פרויקט דוגמה לצ'אטבוט בעברית שמתחבר ל‑OpenAI בצורה בטוחה — בלי לשים מפתחות בקוד או בגיט.<br>
    כולל Backend עם Flask ו‑Frontend HTML/JS עם סיידבר לניהול שיחות.
  </p>

  <p align="right">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Badge">
    <img src="https://img.shields.io/badge/Flask-UI-lightgrey" alt="Flask Badge">
    <img src="https://img.shields.io/badge/HTML%2FJS-Frontend-yellow" alt="HTML/JS Badge">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License Badge">
  </p>

  <hr>

  <h2>📁 מבנה הפרויקט</h2>
  <ul>
    <li><code>main.py</code> — קוד Flask (Backend)</li>
    <li><code>history.json</code> — קובץ שמירה אוטומטית של היסטוריית שיחות</li>
    <li><code>index.html</code> — ממשק משתמש בצד ה‑Frontend</li>
    <li><code>requirements.txt</code> — חבילות נדרשות</li>
    <li><code>.env.example</code> — דוגמת קובץ סביבה</li>
    <li><code>.gitignore</code> — הגדרות Git</li>
  </ul>

  <hr>

  <h2>⚙️ התקנה והרצה</h2>

  <ol>
    <li>צרו וירטואל סביבה (מומלץ):
      <pre><code>python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate</code></pre>
    </li>
    <li>התקנת תלויות:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>צרו קובץ <code>.env</code> על בסיס <code>.env.example</code> והכניסו את ה‑API key שלכם:
      <pre><code>cp .env.example .env
# הכניסו בקובץ .env את המפתח האמיתי במקום הריק</code></pre>
    </li>
    <li>הריצו את השרת:
      <pre><code>python main.py</code></pre>
    </li>
    <li>פתחו את <code>index.html</code> בדפדפן (או על שרת מקומי) כדי להשתמש בצ'אט.<br>
      ⚠️ ודאו ש‑CORS מוגדר נכון ב‑Flask אם אתם מריצים את ה‑HTML מדומיין/פורט אחר.
    </li>
  </ol>

  <hr>

  <h2>📝 תכונות עיקריות</h2>
  <ul>
    <li>שיחות מרובות: יצירה ומחיקה של שיחות בסיידבר</li>
    <li>שמירה אוטומטית: היסטוריית השיחות נשמרת ב‑<code>history.json</code></li>
    <li>טעינה הדרגתית של הודעות: הבוט מקליד תגובה תו אחרי תו</li>
    <li>שפה בעברית: הודעות הבוט מוגדרות בעברית עם נימוס</li>
    <li>אבטחה: מפתחות OpenAI נשמרים בקובץ <code>.env</code>, לא בקוד</li>
  </ul>

  <hr>

  <h2>🔒 אבטחה</h2>
  <ul>
    <li>אסור להעלות את <code>.env</code> ל‑GitHub</li>
    <li>ודאו ש‑<code>.env</code> נמצא ב‑<code>.gitignore</code></li>
    <li>אם העליתם מפתח בטעות — בטלו אותו מה‑OpenAI dashboard וצרו מפתח חדש</li>
  </ul>

  <hr>

  <h2>⚡ שדרוגים מומלצים</h2>
  <ul>
    <li>בניית GUI מתקדם עם <code>tkinter</code> או <code>streamlit</code></li>
    <li>הוספת אפשרות להרצת מודלים אחרים או שינוי פרמטרים (<code>max_tokens</code>, <code>temperature</code>)</li>
    <li>חיבור למאגר נתונים (DB) במקום קובץ JSON לשמירה מתקדמת של היסטוריה</li>
    <li>שיפורי UI/UX: אנימציות נוספות, רספונסיביות, הודעות טעינה משופרות</li>
  </ul>

  <hr>

  <h2>📄 License</h2>
  <p>MIT License © 2025 Raz Eini</p>

</div>
