#  Orb of Day

A task and productivity management backend application developed with **FastAPI**.

This project is being developed throughout my software engineering internship. New features are implemented incrementally and documented daily.

---

# 📖 Project Overview

Orb of Day is a RESTful backend application designed to help users organize daily tasks, improve productivity, and manage their workflow efficiently.

---

# 🛠️ Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- bcrypt
- Uvicorn

---

# 📂 Project Structure

```
Orb_of_Day/
│
├── app/
│   ├── routers/
│   │   ├── user.py
│   │   └── task.py
│   │
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ✅ Completed Features

- FastAPI project setup
- SQLite database integration
- SQLAlchemy ORM configuration
- User database model
- User registration endpoint
- Password hashing using bcrypt
- Swagger API documentation

---

#  Upcoming Features

- User Login
- JWT Authentication
- Protected Routes
- Task CRUD Operations
- AI Task Suggestions
- Dashboard
- Productivity Statistics

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/zerdakyhn/Orb_of_Day.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python -m uvicorn app.main:app --reload
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📅 Internship Progress

## ✅ Days 1–2

### Project Initialization
- Created FastAPI project
- Configured project structure
- Connected SQLite database
- Configured SQLAlchemy
- Created database session
- Created base application
- Configured GitHub repository
- Added project documentation

---

## ✅ Days 3–4

### User Management
- Designed User database model
- Created Pydantic schemas
- Implemented user registration endpoint
- Added password hashing with bcrypt
- Added email validation
- Configured user router
- Tested API using Swagger

---

## ⏳ Next Step (Days 5–6)

### Authentication
- User Login
- Password Verification
- JWT Authentication
- Protected API Endpoints

---

# 📊 Progress

```text
████░░░░░░ 40%
```

Current Phase:
**Backend Development**

---

# 👩‍💻 Developer

**Zerda Kayhan**

Computer Engineering Student

Software Engineering Internship Project

2026

---

# 📄 License

This repository is created for educational and internship purposes.
