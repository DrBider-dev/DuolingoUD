# Duolingo Database Model Project

## 📌 Overview
This project focuses on designing and creating the database structure behind **Duolingo**, a popular language-learning platform. The goal is to analyze and model the core components of Duolingo's system to understand how it manages **users, courses, lessons, and the gamified reward system** that makes it highly engaging for learners.

Duolingo leverages a structured database system to handle large amounts of user data, including **progress tracking, achievements, and language lessons**. By reverse-engineering this system, we aim to create a **comprehensive database model** that could serve as the foundation for similar educational platforms.

---

## 🎯 Goals
- **Analyze** the structure of Duolingo's database.
- **Model** entities, attributes, and relationships to replicate its functionality.
- **Optimize** the design for future implementation in a **relational database management system (RDBMS)**.
- **Document** findings and propose improvements for **educational app development**.

---

## 🛠 Technologies Used
- **MySQL** - Database Management System
- **PostgreSQL** - Database Management System
- **FastAPI** - Web framework for building the API
- **Uvicorn** - ASGI server for running the API
- **Python** - Programming language for the backend logic

---

---

## 🚀 Installation & Setup
To set up and run the project locally, follow these steps:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DrBider-dev/DuolingoUD.git
cd DuolingoDB/src
```

### 2️⃣ Install the dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set up the containers
```bash
docker-compose up
```

### 4️⃣ Run the API
```bash
uvicorn main:app --reload
```

## 🔮 Authors
- [Brayan Estiven Aguirre Aristizabal - 20231020156](https://github.com/DrBider-dev)
- [Marlon Yecid Riveros Guio - 20231020208](https://github.com/Drack678?tab=overview&from=2024-09-01&to=2024-09-15)

