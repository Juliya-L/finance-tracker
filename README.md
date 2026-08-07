# 💰 Finance Tracker API

REST API for personal finance management built with Django REST Framework.

---
## 🌐 Live Demo
(https://web-production-bc986.up.railway.app)


---
## 🚀 Features

- User registration and login
- JWT authentication
- Google OAuth authentication
- Password reset via email
- User profile management
- Income and expense categories
- Transactions CRUD
- Filtering transactions by:
  - category
  - type
  - date range
  - month
  - year
- Monthly analytics and reports
- Budget tracking with progress calculation
- PostgreSQL database
- Swagger/OpenAPI documentation
- Automated API tests with pytest
- Responsive web interface
---

## 🛠 Tech Stack

### Backend
- Python 3.12
- Django 6
- Django REST Framework

### Authentication
- JWT (SimpleJWT)
- Google OAuth2

### Database
- PostgreSQL
- SQLite (local development)

### Testing
- pytest
- pytest-django

### Documentation
- drf-spectacular
- Swagger UI

### Deployment
- Railway
- Gunicorn
- WhiteNoise

### Frontend
- HTML
- CSS
- JavaScript
---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Juliya-L/finance-tracker.git
cd finance-tracker
```

---

### 2. Create virtual environment

#### Windows

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

---

### 5. Run migrations

```bash
python manage.py migrate
```

---

### 6. Start development server

```bash
python manage.py runserver
```

---

## 📖 API Documentation

After starting the server, open:

```txt
http://127.0.0.1:8000/api/docs/
```

Swagger UI is powered by `drf-spectacular`.

---

## 🧪 Running Tests

Run all tests:

```bash
pytest -v
```

Run specific app tests:

```bash
pytest categories/tests.py -v
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register user |
| POST | `/api/auth/token/` | Login |
| POST | `/api/auth/token/refresh/` | Refresh access token |
| GET / PATCH | `/api/auth/me/` | User profile |
| GET / POST | `/api/categories/` | Categories |
| GET / POST | `/api/transactions/` | Transactions |
| GET | `/api/analytics/summary/` | Monthly summary |
| GET | `/api/analytics/by-category/` | Expenses by category |
| GET | `/api/analytics/monthly-trend/` | Monthly trends |
| GET | `/api/analytics/balance/` | Current balance |
| GET / POST | `/api/budgets/` | Budgets |

---

## 🔑 Authentication

Supported authentication methods:

- Email + Password
- Google OAuth2
- JWT Access/Refresh Tokens

Example:

```http
Authorization: Bearer your_access_token
```

## 📧 Password Recovery

Users can reset forgotten passwords via email.

Flow:

1. Enter email address
2. Receive reset link
3. Set new password
4. Login with the new password

## 📂 Project Structure

```txt
users/          # Authentication & users
categories/     # Categories
transactions/   # Transactions
analytics/      # Analytics
budgets/        # Budgets
frontend/       # Templates & UI
config/         # Settings
```

---

## ✅ Testing

The project includes API tests with:

- pytest
- pytest-django
- DRF APIClient
- authentication fixtures
- permissions testing

Example tested scenarios:

- user registration
- JWT authentication
- category CRUD
- permissions & ownership
- transaction filtering

---


## ☁️ Deployment

Production deployment:

- Render Web Service
- Render PostgreSQL Database
- Gunicorn
- WhiteNoise

Live URL:

https://finance-tracker-ev27.onrender.com

---

## 👩‍💻 Author

Personal portfolio project built with Django, PostgreSQL, JavaScript, authentication systems, analytics, and deployment tools.