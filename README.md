# Django Internship Project - Backend System with REST API, Celery, and Telegram Bot

## 🔍 Project Overview

This Django-based backend project demonstrates key skills required for a Python backend internship, including:

- Django REST Framework (DRF) for API development
- Token-based and JWT authentication
- Celery integration with Redis for background task processing
- Telegram bot integration for user interaction
- Clean and production-ready codebase with proper environment management

## ✨ Features

- ✅ Public and protected API endpoints
- 🔒 Token and JWT-based authentication
- 📧 Background email sending using Celery and Redis
- 🤖 Telegram Bot integration to collect usernames
- 🔐 Environment variables for secure configuration
- 🛠️ Production-ready settings with `DEBUG=False`

## 🛠️ Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Authentication:** TokenAuth, JWT (SimpleJWT)
- **Task Queue:** Celery with Redis
- **Telegram Bot:** python-telegram-bot==13.15
- **Deployment Ready:** DEBUG=False, environment-based config

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Create .env file in the root directory**
   **Add the following environment variables:**
   SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=127.0.0.1,localhost
   CELERY_BROKER_URL=redis://localhost:6379/0
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. **Create superuser (to access Django Admin panel)**
   ```bash
   python manage.py createsuperuser

7. **Run the development server**
   ```bash
   python manage.py runserver

8. **Start Celery worker**
   In a new terminal (same project directory):
   ```bash
   celery -A backend_project worker --loglevel=info

⚠️ Note: Replace your-secret-key and your-telegram-bot-token in your .env file.
Do not commit the .env file to GitHub. Use .gitignore to prevent it from being tracked.

## 📡 API Documentation
This project provides both public and protected endpoints using Django REST Framework. JWT and Token-based authentication are supported.

### 🔗 Available Endpoints

| Method | Endpoint             | Description                                | Auth Required  |
|--------|----------------------|--------------------------------------------|----------------|
| GET    | `/api/hello/`        | Public greeting endpoint                   | ❌ No          |
| GET    | `/api/secret/`       | Protected message (uses `IsAuthenticated`) | ✅ Yes         |
| POST   | `/api/register/`     | Register user (triggers Celery email)      | ❌ No          |
| POST   | `/api/send-email/`   | Trigger email via Celery manually          | ❌ No          |
| POST   | `/api/login/`        | Login and get token (TokenAuth)            | ❌ No          |
| POST   | `/api/token/`        | Get JWT token pair                         | ❌ No          |
| POST   | `/api/token/refresh/`| Refresh JWT access token                   | ❌ No          |
| POST   | `/api/token/verify/` | Verify JWT token                           | ❌ No          |

### 🤖 Telegram Bot Commands

The Telegram bot is configured using `python-telegram-bot==13.15`. It listens for the `/start` command and stores the user's Telegram username in the Django database.

> 🧾 You can try the bot here: [@intern_my_bot](https://t.me/intern_my_bot)
Replace @intern_my_bot with your actual bot username if it’s different.

| Command  | Description                                                        |
|----------|--------------------------------------------------------------------|
| `/start` | Collects the user's Telegram username and stores it in the backend |
| `/help`  | Displays a help message                                            |


