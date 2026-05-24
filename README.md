# 💰 Finance Tracker API

REST API for personal finance management built with Django REST Framework.

---

## 🚀 Features

- JWT authentication (register, login, logout)
- Income and expense categories management
- Transactions CRUD with filtering by date, category, and type
- Monthly analytics — balance, summaries, and trends
- Budgets by category with spending progress tracking
- Automatic Swagger/OpenAPI documentation
- Pytest API testing

---

## 🛠 Tech Stack

- Python 3.12
- Django 6 + Django REST Framework
- JWT Authentication (`djangorestframework-simplejwt`)
- PostgreSQL (SQLite for development)
- pytest + pytest-django
- drf-spectacular (Swagger UI)

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

## 🔐 Authentication

This API uses JWT authentication.

Example header:

```http
Authorization: Bearer your_access_token
```

---

## 📂 Project Structure

```txt
accounts/       # Authentication & users
categories/     # Expense/income categories
transactions/   # Financial transactions
analytics/      # Reports and statistics
budgets/        # Budget tracking
config/         # Django settings
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

## 👩‍💻 Author

Backend pet project built for learning Django REST Framework, API architecture, authentication, testing, and financial analytics systems.