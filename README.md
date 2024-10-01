
# Lab_1 in Django Tutorials: Writing my first Django - DRF Course - Hoai Linh 20PFIEV3 - 123200107

## Part_1

Consist of two parts:
- A public site that lets people view polls and vote in them.
- An admin site that lets you add, and delete polls.

### Step 0.1. Check version (no need):
```bash
python -m django --version
```

### Step 0.2. Activate the environment (Specifically for my PC :D):
```bash
source /c/ProgramData/anaconda3/Scripts/activate
conda activate ./env
```

---

### Step 1. Create a project

- Run this command in the directory containing your project:
  ```bash
  django-admin startproject mysite
  ```

- "mysite" is the name we give. For example, I named my project **LinhSite**.

#### Project structure after creation:

```plaintext
LinhSite/
    manage.py
    LinhSite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

Ok, we will talk about each file:
- The **Outer `LinhSite/`**: A container for the entire project. You can rename it.
- The **`manage.py`**: A command-line utility that lets you interact with Django in various ways. (Read more at [django-admin](https://docs.djangoproject.com/en/5.1/ref/django-admin/)). (It's still pretty vague at the moment :v, but I know it's very important to the project.)
- The **Inner `LinhSite/`**: The actual Python package for your project, used to import components (e.g., `LinhSite.urls`).

#### Specific files:
- **`__init__.py`**: An empty file that tells Python this directory should be considered a package.
- **`settings.py`**: Configuration file for the Django project. (Read more at [Django settings](https://docs.djangoproject.com/en/5.1/topics/settings/)).
- **`urls.py`**: The URL declarations for the project (similar to a table of contents for your site). (Read more at [Django URLs](https://docs.djangoproject.com/en/5.1/topics/http/urls/)).
- **`asgi.py`**: The entry-point for ASGI-compatible web servers to serve your project, handling asynchronous tasks. (Read more about [ASGI](https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/)).
- **`wsgi.py`**: The entry-point for WSGI-compatible web servers to serve your project, handling synchronous tasks. (Read more about [WSGI](https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/)).

#### Knowledge on WSGI and ASGI:

- **WSGI (Web Server Gateway Interface)**: A standard interface for web servers and web applications, designed for synchronous tasks. WSGI processes one HTTP request at a time, making it ideal for traditional web frameworks like Django and Flask.

- **ASGI (Asynchronous Server Gateway Interface)**: A newer standard supporting both synchronous and asynchronous applications. ASGI allows handling of multiple tasks concurrently, such as WebSocket connections or asynchronous HTTP requests, making it ideal for real-time applications.

---

### Step 2. Verify project setup

- Run the command:
  ```bash
  python manage.py runserver
  ```

- Result in the browser: Access `http://127.0.0.1:8000/`.
- ![My Result in Step2](./__ProcessImage/Part1Step2.png)
- And my result in Terminal:
```plaintext
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    September 27, 2024 - 02:25:00
    Django version 5.2.dev20240911160443, using settings 'LinhSite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
  ```

- Run the following command to apply the migrations:
  ```bash
  python manage.py migrate
  ```
  
#### Knowledge:
- This is a lightweight web server written purely in Python. We can develop things rapidly and easily.
- Compared with production server - such as Apache or Nginx - with more complicated configuration.
- Django provides the web frameworks for development progress, not web servers for production progress.

---

### Step 3. Create the Polls app

- Run the following command in the same directory as `manage.py`:
  ```bash
  python manage.py startapp polls
  ```
  
#### Knowledge:

- What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

#### App structure for **polls**:
```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

---

### Step 4. Write the first view

- Open the `polls/views.py` file and add the following code:
  ```python
  from django.http import HttpResponse

  def index(request):
      return HttpResponse("I'm Hoai Linh 20PFIEV3, now I'm at the polls index. I've finished Lab_1 For DRF!")
  ```

- This is the most basic view possible in Django. To access it in a browser, we need to map it to a URL. To do this, we need to define a URL configuration, or 'URLconf' for short. These URL configurations are defined inside each Django app, and they are Python files named `urls.py`.

- To define a URLconf for the polls app, create a file `polls/urls.py` with the following content:
  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path("", views.index, name="index"),
  ]
  ```

---

### Step 5. Configure the global URLconf in the LinhSite project to include the URLconf defined in poll urls

- To do this, add an import for `django.urls.include` in `LinhSite/urls.py` and insert an `include()` in the `urlpatterns` list, so we have:
  ```python
  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
      path("polls/", include("polls.urls")),
      path("admin/", admin.site.urls),
  ]
  ```
  
- The `include()` function allows referencing other URLconfs.
  - The `path("polls/", include("polls.urls"))` tells Django: "Whenever the URL starts with `polls/`, look for more URL patterns in the `polls` app's `urls.py` file."
  - Inside the `polls/urls.py`, you can define the specific endpoints for the polls app (e.g., `polls/vote`, `polls/results`), and `include()` will forward the requests to those URLs.
  - **When to use**: When you want to include other URL patterns, but `admin.site.urls` is the only exception to this.

- The `path()` function expects at least two arguments: `route` and `view`.
  - For example, `route: admin/` and `poll/` correspond to different apps, and `view` is the class or function handling the request for the URL that you defined in the `route`.
  
- All of the above processing has ensured that we have wired an index view into the URLconf! Check it by running the command:
  ```bash
  python manage.py runserver
  ```

- Access `http://localhost:8000/polls/` to see the result. Be careful not to confuse this with accessing just `http://localhost:8000/` :v.
- The text “I'm Hoai Linh 20PFIEV3, now I'm at the polls index. I've finished Lab_1 For DRF!”, which I defined in the index view, should appear.
- ![My Result in Step5](./__ProcessImage/Part1Step5.png)

---

### Summary:
In this part of the tutorial, we created a basic Django project, set up a polls app, and configured views and URLs to display the index page.

## Part_2

This tutorial begins where Part 1 left off. We’ll set up the database, create your first model, and get a quick introduction to Django’s automatically-generated admin site.

### Step 1: Set up the Database

- By default, Django uses SQLite. In this project, we will use the default configuration.
- Open `LinhSite/settings.py` and check the **DATABASES** section.
- Set **TIME_ZONE** to your time zone:
  ```python
  TIME_ZONE = 'Asia/Ho_Chi_Minh'
  ```

- Then, run the command to apply migrations for built-in apps:
  ```bash
  python manage.py migrate
  ```

---

### Step 2: Create Models

- Now let’s define the models in `polls/models.py`.

- Open `polls/models.py` and define the models `Question` and `Choice` like this:
  ```python
  from django.db import models

  class Question(models.Model):
      question_text = models.CharField(max_length=200)
      pub_date = models.DateTimeField('date published')

  class Choice(models.Model):
      question = models.ForeignKey(Question, on_delete=models.CASCADE)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)
  ```
  
#### Knowledge:
- Each field in a model is represented by a class variable, and each field maps to a column in the database.

---

### Step 3: Activate the Models

- To activate the `polls` app in your project, you need to include it in `LinhSite/settings.py`.
- Open `LinhSite/settings.py` and add the `PollsConfig` class to the **INSTALLED_APPS** list:
  ```python
  INSTALLED_APPS = [
      'polls.apps.PollsConfig',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

---

### Step 4: Create Migrations

- Run the command to create migrations for the `polls` app:
  ```bash
  python manage.py makemigrations polls
  ```

- Then, run the migration command to apply the changes:
  ```bash
  python manage.py migrate
  ```

- You can also check the generated SQL using the following command:
  ```bash
  python manage.py sqlmigrate polls 0001
  ```

---

### Step 5: Create a Superuser

- Run the following command to create a superuser for the Django admin site:
  ```bash
  python manage.py createsuperuser
  ```
- I entered the following details:
  - Username: `hoailinh`
  - Email: `daohoailinhdn00@gmail.com`
  - Password: `meow@2024`

- After creating the superuser, you should see the following message:
  ```plaintext
  Superuser created successfully.
  ```

---

### Step 6: Activate the Admin Interface for Models

- To make the `Question` model editable in the admin site, register it in `polls/admin.py`.

- Open `polls/admin.py` and add the following code:
  ```python
  from django.contrib import admin
  from .models import Question

  admin.site.register(Question)
  ```

---

### Step 7: Run the Development Server

- Finally, run the development server using:
  ```bash
  python manage.py runserver
  ```

- Open your browser and navigate to `http://127.0.0.1:8000/admin/`.
- Log in using the superuser credentials (`hoailinh`, `meow@2024`), and you will see the `Question` model registered in the admin site.

- Here’s the result in my browser and add new question:
- ![My Result in Part 2](./__ProcessImage/Part2Result.png)
- ![My Result in Part 2](./__ProcessImage/Part2AddNewQuestion.png)

---

### Summary:
In Part 2, we set up the database, created the models, activated them, and registered them in the Django admin site. We also learned how to create migrations and run them to apply model changes.
