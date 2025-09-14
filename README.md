# Django User Profile Project

This is a simple Django project that demonstrates how to create user profile pages using Django templates, template tags, and filters.  
The project includes a list of users and individual profile pages showing additional user information like bio, birthdate, and profile picture.

---

## ✅ Requirements

* Python 3.13.5
* Django==5.2.6

---

## Features

- Display a list of registered users
- View detailed user profile pages
- Use Django template tags (`for`, `if`) to show dynamic content
- Use Django template filters to format and truncate text
- Extend Django's built-in User model with a related Profile model
- Profile images and additional user data

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TAMUNA-CHKOIDZE/django-user-profile.git
   ```

2. Navigate into the project folder:

   ```bash
   cd django-user-profile
   ```
3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations:

   ```bash
   python manage.py migrate
   ```
6. Start the development server:

   ```bash
   python manage.py runserver
   ```

---

## Usage

* Visit `http://127.0.0.1:8000/users/` to see the list of users.
* Click on a user card to view their profile details.
* Profiles display additional information.

---

## Notes

* This project uses Django's built-in `User` model extended with a `Profile` model.
* Make sure to add profile images in the admin panel or extend registration flow accordingly.

---

## License

This project is open source and free to use.

---

## Author

Tamuna Chkoidze

```


