<div dir="rtl">

  <h1 align="right">🤖 SmartChat — Secure Hebrew Chatbot</h1>

  <p>
    פרויקט <strong>SmartChat</strong> הוא צ'אטבוט חכם בעברית, המתחבר ל־OpenAI API בצורה מאובטחת וללא חשיפת מפתחות.<br>
    המערכת כוללת Backend ב־<strong>Flask</strong> ו־Frontend אינטראקטיבי ב־<strong>HTML/JS</strong> עם ניהול שיחות, שמירה אוטומטית וטעינה מהירה.
  </p>

  <p align="right">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Badge">
    <img src="https://img.shields.io/badge/Flask-Backend-lightgrey" alt="Flask Badge">
    <img src="https://img.shields.io/badge/HTML%2FJS-Frontend-yellow" alt="HTML/JS Badge">
    <img src="https://img.shields.io/badge/OpenAI-Integration-green" alt="OpenAI Badge">
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
        <td>שרת Flask – אחראי על ניהול בקשות, שיחות ותקשורת עם OpenAI</td>
      </tr>
      <tr>
        <td><code>static/</code></td>
        <td>קבצי עיצוב ו־JavaScript של ה־Frontend</td>
      </tr>
      <tr>
        <td><code>templates/index.html</code></td>
        <td>עמוד הצ’אט הראשי (UI)</td>
      </tr>
      <tr>
        <td><code>history.json</code></td>
        <td>שמירת היסטוריית השיחות המקומית</td>
      </tr>
      <tr>
        <td><code>.env</code></td>
        <td>שמירת מפתח OpenAI בצורה מאובטחת (לא נכלל ב־Git)</td>
      </tr>
      <tr>
        <td><code>requirements.txt</code></td>
        <td>רשימת הספריות הדרושות להרצה</td>
      </tr>
      <tr>
        <td><code>.gitignore</code></td>
        <td>מונע העלאה של קבצי סביבה או קונפיגורציה רגישים</td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>🧠 Features</h2>

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
        <td>💬 ניהול שיחות</td>
        <td>מעבר בין שיחות ישנות וחדשות בסיידבר</td>
        <td>✅</td>
        <td>טעינה ושמירה אוטומטית</td>
      </tr>
      <tr>
        <td>💾 שמירת נתונים</td>
        <td>שמירת היסטוריית הצ'אט ל־<code>history.json</code></td>
        <td>✅</td>
        <td>נשמר מקומית במחשב</td>
      </tr>
      <tr>
        <td>⌨️ טעינה הדרגתית</td>
        <td>הבוט מקליד תגובה תו־תו (אנימציית typing)</td>
        <td>✅</td>
        <td>מעניק תחושת טבעיות</td>
      </tr>
      <tr>
        <td>🌐 תמיכה מלאה בעברית</td>
        <td>תמיכה ב־RTL ותגובות טבעיות בעברית</td>
        <td>✅</td>
        <td>מותאם לעברית מלאה</td>
      </tr>
      <tr>
        <td>🔒 אבטחה</td>
        <td>שמירת מפתח OpenAI בקובץ .env</td>
        <td>✅</td>
        <td>לא נחשף בקוד</td>
      </tr>
      <tr>
        <td>🧩 אינטגרציה עם OpenAI</td>
        <td>שימוש ב־API של OpenAI לתקשורת בזמן אמת</td>
        <td>✅</td>
        <td>תומך ב־GPT-5 ומעלה</td>
      </tr>
      <tr>
        <td>🎨 ממשק משתמש</td>
        <td>UI רספונסיבי עם עיצוב נקי ומודרני</td>
        <td>✅</td>
        <td>HTML + CSS + JS</td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>💡 דוגמת קובץ <code>.env.example</code></h2>
  <pre><code>OPENAI_API_KEY="הכניסו כאן את המפתח שלכם"</code></pre>

  <hr>

  <h2>⚙️ התקנה / Installation</h2>

  <table>
    <tr>
      <td><strong>שלב 1:</strong> התקנת הספריות הדרושות</td>
      <td><code>pip install -r requirements.txt</code></td>
    </tr>
    <tr>
      <td><strong>שלב 2:</strong> יצירת קובץ .env</td>
      <td>העתק את <code>.env.example</code> והוסף את מפתח ה־OpenAI שלך</td>
    </tr>
    <tr>
      <td><strong>שלב 3:</strong> הרצת השרת</td>
      <td><code>python app.py</code></td>
    </tr>
    <tr>
      <td><strong>שלב 4:</strong> פתיחת הממשק</td>
      <td>גלוש אל <code>http://localhost:5000</code></td>
    </tr>
  </table>

  <hr>

  <h2>🛠️ Tech Stack</h2>
  <ul>
    <li><strong>Backend:</strong> Flask (Python)</li>
    <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
    <li><strong>API:</strong> OpenAI GPT-5</li>
    <li><strong>Storage:</strong> JSON (לשמירת היסטוריית שיחות)</li>
  </ul>

  <hr>

  <h2>🔒 אבטחה</h2>
  <ul>
    <li>אין לשתף או להעלות את קובץ <code>.env</code> ל-GitHub.</li>
    <li>ודאו שהוא מופיע בקובץ <code>.gitignore</code>.</li>
    <li>אם מפתח דלף – בטלו אותו מיד דרך <strong>OpenAI Dashboard</strong> וצור חדש.</li>
  </ul>

  <hr>

  <h2>📄 רישיון</h2>
  <p>
    הפרויקט מופץ תחת רישיון <strong>MIT</strong> – חופשי לשימוש, שינוי והפצה, כל עוד נשמר קרדיט למחבר.
  </p>
  <p>למידע נוסף ראה את קובץ <a href="LICENSE">LICENSE</a></p>

  <hr>

  <p><strong>👨‍💻 Raz Eini (2025)</strong></p>

