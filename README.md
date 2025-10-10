  <h1>🤖 SmartChat — Secure Hebrew Chatbot</h1>

  <p>
    פרויקט דוגמה לצ'אטבוט בעברית שמתחבר ל‑OpenAI בצורה בטוחה — בלי לשים מפתחות בקוד או בגיט.<br>
    כולל Backend עם Flask ו‑Frontend HTML/JS עם סיידבר לניהול שיחות.
  </p>

  <p align="right">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Badge">
    <img src="https://img.shields.io/badge/Flask-Backend-lightgrey" alt="Flask Badge">
    <img src="https://img.shields.io/badge/HTML%2FJS-Frontend-yellow" alt="HTML/JS Badge">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License Badge">
  </p>

  <hr>

  <h2>📁 מבנה הפרויקט</h2>
  <ul>
    <li><code>app.py</code> — קוד Flask (Backend)</li>
    <li><code>history.json</code> — קובץ שמירה אוטומטית של היסטוריית שיחות</li>
    <li><code>index.html</code> — ממשק משתמש בצד ה‑Frontend</li>
    <li><code>requirements.txt</code> — חבילות נדרשות</li>
    <li><code>.env.example</code> — דוגמת קובץ סביבה</li>
    <li><code>.gitignore</code> — הגדרות Git</li>
  </ul>

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

  <h2>📄 License</h2>
  <p>MIT License © 2025 Raz Eini</p>
