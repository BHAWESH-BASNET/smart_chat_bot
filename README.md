# 🤖 SmartChat — Secure Python Chatbot (עברית)


פרויקט דוגמה לצ'אטבוט בעברית שמתחבר ל־OpenAI בצורה בטוחה — בלי לשים מפתחות בקוד או בגיט.


## מבנה


- `main.py` — קוד הבוט
- `requirements.txt` — חבילות נדרשות
- `.env.example` — דוגמת קובץ סביבה
- `.gitignore` — הגדרות גיט


## התקנה והרצה


1. צרו וירטואל סביבה (מומלץ):


```bash
python -m venv venv
source venv/bin/activate # Linux / macOS
venv\Scripts\activate # Windows
```


2. התקנת תלויות:


```bash
pip install -r requirements.txt
```


3. צרו קובץ `.env` על בסיס `.env.example` והכניסו את ה־API key שלכם:


```bash
cp .env.example .env
# ואז תשימו בקובץ .env את המפתח האמיתי במקום הריק
```


4. הריצו את הבוט:


```bash
python main.py
```


## אבטחה


- **אסור** להעלות את `.env` ל־GitHub.
- הוסיפו `.env` ל־`.gitignore` (כבר במיזם הזה).
- אם העליתם מפתח בטעות — בטלו אותו מה־OpenAI dashboard וצרו מפתח חדש.


## שדרוגים מומלצים


- שמירת היסטוריית שיחות לקובץ הצפוי (לניתוח)
- בניית GUI עם `tkinter` או `streamlit`
- הוספת אפשרות להרצת מודלים אחרים/שינוי פרמטרים


---
# License


MIT License © 2025 Raz Eini