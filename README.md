# Student Management Portal

This is a simple Django-based web application for managing student records. It allows users to add, update, list, and delete students from the system.


## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/student-management-portal.git
cd student-management-portal
```

### 2. Create and activate a Python virtual environment.

- Linux 
```       
python3 -m venv venv
source venv/bin/activate
```
- Windows

``` 
python -m venv venv
.\venv\Scripts\activate
``` 

### 3. Install Required Dependencies

``` 
pip install -r requirements.txt
``` 

### 4. Configure Database
``` 
python manage.py makemigrations
``` 

### 6. Apply Migrations
``` 
python manage.py migrate
``` 

### 7. Run the Development Server
``` 
python manage.py runserver
``` 

### 8. Create Superuser (Optional)
``` 
python manage.py createsuperuser
``` 

### 9 Project Structure

``` student-management-portal/
├── student_management/          # Django project settings
│   ├── __init__.py
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Project URLs
│   └── wsgi.py                  # WSGI application
├── students/                    # Django app for students
│   ├── __init__.py
│   ├── admin.py                 # Admin configuration
│   ├── apps.py                  # App configuration
│   ├── models.py                # Student model
│   ├── views.py                 # Views for handling logic
│   ├── urls.py                  # App-specific URLs
│   └── migrations/              # Database migrations
└── manage.py                    # Django management commands

``` 