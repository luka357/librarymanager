# Library Manager

A Django web app for managing a library's books and authors. Every page is behind login, and each resource has full CRUD through server-rendered templates.

## Features

- 🔐 Login and logout with Django's built-in authentication
- 📚 Books: add, view, edit and delete (title, author, page count, description)
- ✍️ Authors: add, view, edit and delete (name and bio)
- 🛡️ All views protected with `@login_required`
- ModelForms for validated input

## Tech Stack

**Backend:** Python, Django
**Frontend:** Django Templates, HTML
**Database:** SQLite

## Getting Started

```bash
git clone https://github.com/luka357/librarymanager.git
cd librarymanager
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/login/ and sign in with the user you created.

## Routes

| URL | Description |
|---|---|
| `/login/`, `/logout/` | Authentication |
| `/books/` | Book list |
| `/books/add/` | Add a book |
| `/books/<id>/` · `/update/` · `/delete/` | View, edit, delete a book |
| `/authors/` | Author list and the same CRUD routes as books |
| `/admin/` | Django admin |

## Project Structure

- `core/` — project settings and root URLs
- `books/` — `Book` model, forms, views and templates
- `authors/` — `Author` model, forms, views and templates
- `templates/registration/` — login page

## Author

**Luka Julakidze**
[LinkedIn](https://www.linkedin.com/in/luka-julakidze) · [GitHub](https://github.com/luka357)
