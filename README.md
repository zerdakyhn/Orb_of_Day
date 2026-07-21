# 🚀 Orb of Day

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green?logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![JWT](https://img.shields.io/badge/JWT-Authentication-black)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

---

A modern **Task & Productivity Management RESTful API** built with **FastAPI**.

Orb of Day is a backend application that enables users to securely manage daily tasks through a clean, scalable and maintainable architecture.

The project follows modern RESTful API principles and is designed with future scalability and AI-powered productivity features in mind.

---

# ✨ Features

## 👤 User Management

- User Registration
- User Login
- User Profile Update
- Change Password
- User Logout
- Email Validation
- Username Validation
- Password Hashing using bcrypt

## 🔐 Authentication

- JWT Authentication
- JWT Access Token Generation
- Protected API Endpoints
- OAuth2 Authentication
- Secure Password Verification

## ✅ Task Management

- Create Task
- Update Task
- Delete Task
- Task Status Update
- User–Task Relationship
- Task Database Model

## ⚙️ Backend

- RESTful API
- SQLAlchemy ORM
- SQLite Database
- Swagger Documentation
- Pydantic Validation
---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| SQLAlchemy | ORM |
| SQLite | Database |
| Pydantic | Data Validation |
| bcrypt | Password Hashing |
| python-jose | JWT Authentication |
| Uvicorn | ASGI Server |
| Git | Version Control |
| GitHub | Source Code Management |

---

# 🏗️ System Architecture

```text
                 Client
                    │
                    ▼
             FastAPI REST API
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
 Authentication             Task Module
       │                         │
       └────────────┬────────────┘
                    ▼
              SQLAlchemy ORM
                    │
                    ▼
               SQLite Database
```

---

# 🗄️ Database Design

```text
+----------------------+
|        USERS         |
+----------------------+
| id                   |
| username             |
| email                |
| hashed_password      |
| created_at           |
+----------------------+
           │
           │ 1
           │
           ▼
          N
+----------------------+
|        TASKS         |
+----------------------+
| id                   |
| title                |
| description          |
| completed            |
| created_at           |
| owner_id (FK)        |
+----------------------+
```

---

# 📂 Project Structure

```text
Orb_of_Day
│
├── app
│   ├── routers
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

# 🌐 API Endpoints

| Method | Endpoint | Description | Status |
|---------|----------|-------------|--------|
| POST | `/users/register` | Register User | ✅ |
| POST | `/users/login` | Login User | ✅ |
| GET | `/users/me` | Get Current User | ✅ |
| PUT | `/users/me` | Update User Profile | ✅ |
| POST | `/users/change-password` | Change Password | ✅ |
| POST | `/users/logout` | Logout | ✅ |
| POST | `/tasks` | Create Task | ✅ |
| PUT | `/tasks/{id}` | Update Task | ✅ |
| DELETE | `/tasks/{id}` | Delete Task | ✅ |
| GET | `/tasks` | Get User Tasks | ⏳ |

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/zerdakyhn/Orb_of_Day.git
```

Go to project directory

```bash
cd Orb_of_Day
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

macOS / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install requirements

```bash
pip install -r requirements.txt
```

Run the project

```bash
python -m uvicorn app.main:app --reload
```

---

# 📚 API Documentation

After starting the application, open:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows testing every endpoint.

---

# 📈 Development Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 | ✅ Completed |
| Sprint 2 Days 1–2 | ✅ Completed |
| Sprint 2 Days 3–4 | ✅ Completed |
| Sprint 2 Days 5–6 | ✅ Completed |
| Sprint 3 | ⏳ In Progress |

--

# 🚀 Roadmap

- ✅ User Registration
- ✅ User Login
- ✅ JWT Authentication
- ✅ User Profile Update
- ✅ Change Password
- ✅ Logout
- ✅ Task Model
- ✅ Task Creation
- ✅ Task Editing
- ✅ Task Deletion
- ✅ Task Status Update
- ⏳ Task Authorization
- ⏳ Get User Tasks
- ⏳ Dashboard
- ⏳ AI Productivity Assistant

---

# 📊 Project Status

Current Phase

**Backend Development**

Overall Progress

```text
████████░░ 80%

---


# 👩‍💻 Developer

**Zerda Kayhan**

GitHub

https://github.com/zerdakyhn

---

# 📄 License

This project is intended for educational and portfolio purposes.
