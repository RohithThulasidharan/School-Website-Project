# School-Website-Project

A web project based on Django and managing a database stored on PostgreSQL. A database schema was first made in Postgres and it was later imported to the Django project.

## Project content
Django project name: "schoolproject"

and Django App created: "authentication"

## Installation Requirements
1. PostgreSQL
2. Python Virtual Environment
```bash
python -m venv venv
```

3. Django
```bash
pip install django
```


##Usage
The project folder is in a python virtual environment. Open the shell, go to the root directory (contains 'venv' folder) and activate the virtual environment 'venv'.
```bash
venv\scripts\activate
```

This will activate the virtual environment. Next, in the root directory (contains 'manage.py' folder), execute the command 
```bash
python manage.py runserver
```
This will run the server in the local machine with the address of http://127.0.0.1:8000/. 
Type the address in your browser and it will open the website.

You can sign up and sign in to the site. After signing in, you have the options to
1. View a student's marks using his student ID.
2. View the rank list of a class by typing in the Classroom ID.
3. Add a new student to the database.
