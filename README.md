# Lawyers2Go API (Django)

Django port of the Lawyers2Go API. 

## Structure (module monolith)

- **config/** – Project settings, URLs, WSGI/ASGI
- **modules/** – Domain apps (one app per domain, single codebase):
  - **accounts** – Auth, User, Role, Provider, Client, Upload
  - **geo** – Country, State, County, City, CityRate, StateSubscriptionRate
  - **catalog** – Category, Function, ServiceType, Service, ServiceFee
  - **cases** – Case, Quote
  - **orders** – Order, Invoice, Transaction
  - **reviews** – Review
  - **messaging** – Conversation, Message
  - **notifications** – Notification
  - **payments** – Payment (Stripe, tax, etc.)
  - **subscriptions** – Plan, Subscription, SubscriptionTier, Package, Coupon, UserSubscription
  - **availability** – Availability
  - **contact** – Contact Us
  - **settings_app** – Settings

## Setup

1. **Create virtualenv and install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your MySQL credentials and DJANGO_SECRET_KEY
   ```

3. **Database**
   - Ensure MySQL is running and the database exists (or create it).
   - Run migrations:
     ```bash
     python manage.py migrate
     ```
   - If you are reusing the same DB as the old Express app, you may need to run migrations with `--fake` for existing tables and then add any new tables.

4. **Run the server**
   ```bash
   python manage.py runserver 8081
   ```
   API is at `http://localhost:8081/` (path prefixes: `/auth/`, `/users/`, `/order/`, etc.).

## API endpoints

Same path structure as the Express API:

- `/auth/` – register, login (web, app, admin, Facebook, Google, Apple)
- `/role/` – CRUD roles
- `/users/` – users, providers, clients, profile, OTP, password, admin
- `/category/`, `/function/`, `/serviceType/`, `/service/`, `/service-fee/`
- `/country/`, `/state/`, `/county/`, `/city/`, `/city-rate/`, `/state-subscription-rate/`
- `/case/`, `/quote/`
- `/order/`, `/invoice/`, `/transaction/`
- `/review/`, `/notification/`, `/conversation/`, `/message/`
- `/upload/`, `/availability/`, `/payment/`
- `/plan/`, `/subscription/`, `/subscription-tier/`, `/packages/`, `/coupons/`, `/user-subscription/`
- `/contact-us/`, `/settings/`

JWT auth is used via `djangorestframework-simplejwt` (e.g. `Authorization: Bearer <token>`).

## Requirements

- Python 3.9+
- MySQL 5.7+ (or 8.x)
- See `requirements.txt` for Python packages.
