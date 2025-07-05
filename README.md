# 📝 Flask Task Manager

A beginner-friendly Flask web app for managing personal tasks, with login/signup functionality, password hashing, error handling, and modular code structure using Blueprints.

---

## 🚀 Features

- ✅ User Signup & Login (with password hashing)(session management)
- ✅ Task CRUD (Create, Read, Update, Delete)
- ✅ SQLite database
- ✅ CSS Styling
- ✅ Error handling
- ✅ Modular structure using Blueprints

---

## 📁 Project Structure
task_manager/
├── app.py
├── config.py
├── db.py
├── auth/
│ ├── init.py
│ └── routes.py
├── tasks/
│ ├── init.py
│ └── routes.py
├── templates/
│ ├── base.html, login.html, signup.html, etc.
├── static/
│ └── style.css
├── init_db.py
├── requirements.txt
└── README.md

---

## 📦 Requirements

- Python 3.8 or newer
- `pip`
- Virtual environment support

Install requirements:
```bash
pip install -r requirements.txt

---

## 🛠️ Setup/Run:
```bash
cd project-folder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt (or pip install Flask , pip install Werkzeug)
python init_db.py
python app.py

Then open: http://localhost:5000