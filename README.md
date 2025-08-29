# TripEase - Travel Booking Application

## Overview
TripEase is a Django-based travel booking application that allows users to view travel options, book tickets, and manage their bookings. Additionally, merchants can manage travel services through a dedicated dashboard.

---

## Core Features

### User Features
- Registration, login, logout, and profile management
- Browse available travel options (Flight, Train, Bus) with filters
- Book tickets and view/cancel current or past bookings

### Merchant Features
- Merchant signup, login, and dashboard
- Add, edit, and delete vehicle types and schedules
- Manage bookings for their services

### Frontend
- Responsive UI using Django templates and CSS
- Basic styling for usability

---

## Project Structure

TripEase/
├── TripEase/ # Project settings
├── core/ # User app
├── merchant/ # Merchant app
├── templates/ # HTML templates
├── static/ # CSS, JS, images
└── manage.py


---

## Setup Instructions

1. **Clone the repository**
```
git clone <REPO_URL>
cd TripEase
```

2. **Create a virtual environment and activate**

```python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

3. **Install dependencies**

```pip install -r requirements.txt ```

4. **Configure database**
``` Update TripEase/settings.py with your MySQL credentials (if using MySQL). Default SQLite works without changes. ```

``` Run migrations ```

```python manage.py makemigrations ```
```python manage.py migrate ```


5. **Collect static files**

```python manage.py collectstatic ```


6. **Run locally**

``` python manage.py runserver ``` 


``` Visit http://127.0.0.1:8000```



**Notes**

Always run collectstatic after changing CSS or JS

Ensure migrations are applied after updating models

Merchant dashboard adds extended functionality beyond the core assignment

**Author**
```0XBHR4JJ```
Deployed URL: https://xbhi12.pythonanywhere.com
