# 🏠 Hostel Management System | FastAPI + MongoDB

A modern full-stack web application for managing hostel operations efficiently using FastAPI, MongoDB, HTML, CSS and JavaScript.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen?style=for-the-badge&logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A modern full-stack **Hostel Management System** built using **FastAPI, MongoDB, HTML, CSS, and JavaScript**. This project streamlines hostel administration by providing a centralized platform for managing students, rooms, complaints, and administrative operations.

---

# 📸 Preview

> **Screenshots will be added after deployment.**

- Login Page
- Student Dashboard
- Admin Dashboard
- Room Allocation
- Complaint Management

---

# 🌐 Live Demo

🚧 **Coming Soon**

---

# ✨ Features

## 👨‍🎓 Student Module

- ✅ Student Login
- ✅ View Profile
- ✅ View Room Allocation
- ✅ Submit Complaints
- ✅ View Notices
- ✅ Leave Request *(Planned)*

---

## 👨‍💼 Admin Module

- ✅ Dashboard
- ✅ Manage Students
- ✅ Manage Rooms
- ✅ Allocate Rooms
- ✅ Manage Complaints
- ✅ Manage Hostel Records

---

## 🏢 Warden Module *(Planned)*

- Leave Approval
- Complaint Management
- Hostel Occupancy Monitoring

---

# 🛠 Tech Stack

## Backend

- FastAPI
- Python

## Frontend

- HTML5
- CSS3
- JavaScript

## Database

- MongoDB

## Version Control

- Git
- GitHub

---

# 🏗 System Architecture

```text
                Browser
                   │
                   ▼
        HTML • CSS • JavaScript
                   │
                   ▼
              FastAPI Backend
                   │
                   ▼
              MongoDB Database
```

---

# 📂 Project Structure

```text
hostel-system/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── routes/
│   ├── models/
│   ├── requirements.txt
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── index.html
│
├── .gitignore
└── README.md
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/Ashwin-vg/hostel-system.git
cd hostel-system
```

## Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/login` | User Login |
| GET | `/students` | Retrieve Students |
| POST | `/students` | Add Student |
| GET | `/rooms` | Retrieve Rooms |
| POST | `/complaints` | Submit Complaint |

> *Update this table as you add more APIs.*

---

# 🔒 Security

### Current

- Input Validation
- Secure API Design

### Planned

- JWT Authentication
- Password Hashing (Argon2/Bcrypt)
- Role-Based Access Control (RBAC)
- Refresh Tokens
- Rate Limiting
- Audit Logging

---

# 📈 Roadmap

## Version 1.0

- [x] Student Management
- [x] Room Management
- [x] Complaint Module
- [x] Admin Dashboard

## Version 2.0

- [ ] JWT Authentication
- [ ] Role-Based Access
- [ ] Password Reset
- [ ] Email Verification
- [ ] Warden Module

## Version 3.0

- [ ] Docker Support
- [ ] GitHub Actions
- [ ] Deployment
- [ ] Analytics Dashboard
- [ ] Real-Time Notifications
- [ ] QR Visitor Pass

---

# 📚 Skills Demonstrated

- REST API Development
- Backend Development
- CRUD Operations
- Database Design
- FastAPI
- MongoDB
- HTML/CSS/JavaScript
- Git & GitHub
- Software Engineering Fundamentals

---

# 🤝 Contributing

Contributions are welcome.

1. Fork this repository
2. Create your feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Ashwin V G**

📧 Email: ashwinvg.cyber@gmail.com

🔗 GitHub: https://github.com/Ashwin-vg

🔗 LinkedIn: https://www.linkedin.com/in/ashwin-v-g

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further development.

---

## 🚀 Future Vision

This project is being developed as a production-inspired hostel management platform that follows modern software engineering practices.

Upcoming improvements include:

- Secure Authentication & Authorization
- Docker Containerization
- CI/CD with GitHub Actions
- Cloud Deployment
- Automated Testing
- Responsive UI
- Analytics Dashboard
- Comprehensive Documentation

---

⭐ If you found this project helpful, don't forget to star the repository.
