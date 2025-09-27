# Django User Profile Project

This is a simple Django project that demonstrates how to create user profile pages using Django templates, template
tags, and filters.
The project includes a list of users, individual profile pages showing additional user information like bio, birthdate,
and profile picture,
and management of user posts linked to profiles.

---

## ✅ Requirements

* Python 3.13.5
* Django==5.2.6

---

## Features

* Display a list of registered users
* View detailed user profile pages
* Use Django template tags (`for`, `if`) to show dynamic content
* Use Django template filters to format and truncate text
* Extend Django's built-in `User` model with a related `Profile` model
* Manage user posts with a `Post` model linked to profiles
* Profile images and additional user data
* **Create, update, and soft delete user posts**

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
* Profiles display additional information including bio, birthdate, location, and posts.
* Users can create new posts, edit existing posts, and soft delete posts (posts are hidden instead of permanently removed).

---

## Notes

* This project uses Django's built-in `User` model extended with a related `Profile` model to store additional user
  information.
* User-generated content is managed through a `Post` model linked to the profiles, allowing users to share posts with
  images and captions.
* Soft delete is implemented for posts to prevent permanent data loss.
* Make sure to add profile images and cover photos in the admin panel or extend the registration flow accordingly.

---

## License

This project is open source and free to use.

---

## Author

Tamuna Chkoidze

---

```markdown
## Future Improvements

- Add user registration and authentication flows.
- Implement editing functionality for user profiles and posts.
- Add pagination for posts and user lists.
- Enhance the UI/UX with better styling and responsive design.
```




