# 🚀 Orb of Day

A modern task and productivity management backend application built with **FastAPI**.

Orb of Day is a RESTful API designed to help users organize their daily tasks, manage productivity, and support future AI-powered recommendations.

The project follows modern backend development practices including layered architecture, secure authentication, and scalable API design.

---

# 📖 Project Overview

Orb of Day aims to provide a clean and scalable backend for a productivity application.

Current focus areas include:

- User Management
- Authentication & Security
- Task Management
- RESTful API Development
- AI Integration (Upcoming)

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| SQLAlchemy | ORM |
| SQLite | Database |
| Pydantic | Data Validation |
| bcrypt | Password Hashing |
| Uvicorn | ASGI Server |

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

# ✨ Current Features

### User Management

- User database model
- User registration endpoint
- Email validation
- Secure password hashing using bcrypt

### Backend

- FastAPI application structure
- SQLAlchemy integration
- SQLite database
- RESTful API architecture
- Swagger API documentation

---

# 🚧 Planned Features

### Authentication

- User Login
- JWT Authentication
- Protected Routes

### Task Management

- Create Task
- Update Task
- Delete Task
- Complete Task
- Task Categories
- Due Dates

### Productivity

- Dashboard
- Statistics
- Daily Progress
- Productivity Reports

### Artificial Intelligence

- AI Task Suggestions
- Smart Productivity Analysis
- Personalized Recommendations

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/zerdakyhn/Orb_of_Day.git
```

Move into the project directory

```bash
cd Orb_of_Day
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m uvicorn app.main:app --reload
```

---

# 📚 API Documentation

After starting the server, Swagger UI is available at:

```
http://127.0.0.1:8000/docs
```

---

# 📈 Development Progress

## ✅ Days 1–2

### Project Foundation

- Created FastAPI project
- Configured application architecture
- Integrated SQLAlchemy
- Connected SQLite database
- Configured project structure
- Created GitHub repository
- Added project documentation

---

## ✅ Days 3–4

### User Management

- Designed User database model
- Created Pydantic schemas
- Implemented user registration endpoint
- Added password hashing using bcrypt
- Added email validation
- Configured user router
- Tested API using Swagger

---

## 🔜 Next Milestone (Days 5–6)

### Authentication

- User Login
- Password Verification
- JWT Token Generation
- Protected API Endpoints

---

# 📊 Project Status

**Current Phase**

Backend Development

**Overall Progress**

```text
████░░░░░░ 40%
```

---

# 👩‍💻 Developer

**Zerda Kayhan**

Computer Engineering Student

---

# 📄 License

This project is available for educational and portfolio purposes.


