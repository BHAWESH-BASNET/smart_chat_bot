<div dir="rtl">

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

  <table>
    <thead>
      <tr>
        <th>קובץ/תיקייה</th>
        <th>תיאור</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>app.py</code></td>
        <td>קוד Flask (Backend)</td>
      </tr>
      <tr>
        <td><code>history.json</code></td>
        <td>שמירה אוטומטית של היסטוריית שיחות</td>
      </tr>
      <tr>
        <td><code>index.html</code></td>
        <td>ממשק Frontend</td>
      </tr>
      <tr>
        <td><code>requirements.txt</code></td>
        <td>חבילות נדרשות</td>
      </tr>
      <tr>
        <td><code>.env.example</code></td>
        <td>דוגמת קובץ סביבה</td>
      </tr>
      <tr>
        <td><code>.gitignore</code></td>
        <td>הגדרות Git</td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>📝 תכונות עיקריות</h2>

  <table>
    <thead>
      <tr>
        <th>תחום</th>
        <th>תכונה</th>
        <th>סטטוס</th>
        <th>הערות</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>💬 שיחות מרובות</td>
        <td>יצירה ומחיקה של שיחות בסיידבר</td>
        <td>✅</td>
        <td>UI נוח למעבר בין שיחות</td>
      </tr>
      <tr>
        <td>💾 שמירה אוטומטית</td>
        <td>היסטוריית השיחות נשמרת ב‑<code>history.json</code></td>
        <td>✅</td>
        <td>טעינה מחדש בעת פתיחת הפרויקט</td>
      </tr>
      <tr>
        <td>⌨️ טעינה הדרגתית</td>
        <td>הבוט מקליד תגובה תו אחרי תו</td>
        <td>✅</td>
        <td>מראה טבעי יותר</td>
      </tr>
      <tr>
        <td>📝 עברית</td>
        <td>הודעות הבוט בעברית מנומסת</td>
        <td>✅</td>
        <td>לשפה טבעית וקריאה</td>
      </tr>
      <tr>
        <td>🔒 אבטחה</td>
        <td>מפתחות OpenAI נשמרים בקובץ <code>.env</code></td>
        <td>✅</td>
        <td>לא בקוד או בגיט</td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>💡 דוגמת קוד .env.example </h2>
  <pre><code>OPENAI_API_KEY="שימו פה את המפתח שלכם"</code></pre>

  <hr>

  <h2>⚙️ התקנה</h2>

  <table>
    <tr>
      <td><strong>שלב 1:</strong> התקנת חבילות</td>
      <td><code>pip install -r requirements.txt</code></td>
    </tr>
    <tr>
      <td><strong>שלב 2:</strong> יצירת קובץ .env</td>
      <td>העתק מ‑<code>.env.example</code> והוסף את מפתח ה‑OpenAI שלך</td>
    </tr>
    <tr>
      <td><strong>שלב 3:</strong> הרצת הפרויקט</td>
      <td><code>python app.py</code></td>
    </tr>
  </table>

  <hr>

  <h2 align="right">🛠️ Tech Stack</h2>
  <ul>
    <li><strong>שפה:</strong> Python 3.8+</li>
    <li><strong>Framework:</strong> Flask</li>
    <li><strong>Frontend:</strong> HTML/JS</li>
  </ul>

  <hr>

  <h2>🔒 אבטחה</h2>
  <ul>
    <li>אל תעלה את <code>.env</code> ל‑GitHub</li>
    <li>ודא שהוא מופיע ב‑<code>.gitignore</code></li>
    <li>אם מפתח דלף, בטל אותו ב‑OpenAI Dashboard וצור חדש</li>
  </ul>

  <hr>

  <h2>📄 License</h2>
  <p>MIT License © 2025 Raz Eini</p>

</div>
