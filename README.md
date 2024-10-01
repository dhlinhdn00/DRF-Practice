
# Lab_1 in Django Tutorials: Writing my first Django - DRF Course - Hoai Linh 20PFIEV3 - 123200107

## Part_1

### Step 0.1. Check version (no need):

    python -m django --version

### Step 0.2. Activate the environment (Specifically for my PC :D):

    source /c/ProgramData/anaconda3/Scripts/activate

    conda activate ./env


### Step 1. Create a project (Run this command in directory coining your project):

    django-admin starproject mysite

With 'mysite' is the name you give. For example, I want to name my project LinhSite - Pas problème! 

At this time, my project 's structure:

    LinhSite/
        manage.py
        LinhSite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py

Ok, we will talk about each file:
    The outer 'LinhSite/': A container for my project. We can rename it to anything.
    The 'manage.py': A command-line utility that lets me interact wiwth this Django in various ways. Read more in https://docs.djangoproject.com/en/5.1/ref/django-admin/ . 
    (It's still pretty vague at the moment :v, but I know it's very important to the project.)
    The inner 'LinhSite/': The actual Python package for my project. Use for importing anything inside it (e.g. LinhSite.urls)
    The 'LinhSite/__init__.py': An empty file that tells Python that this directory should be considered a Python package. Read more in https://docs.python.org/3/tutorial/modules.html#tut-packages .
    The 'LinhSite/setting.py': Settings/configuration for this Django project. Read more in https://docs.djangoproject.com/en/5.1/topics/settings/ .
    The 'LinhSite/urls.py': The URL declarations for this Django project, just like, a table of contents. Read more in https://docs.djangoproject.com/en/5.1/topics/http/urls/ .
    The 'LinhSite/asgi.py': An Entry-point for ASGI-compatible web servers to serve my project. Read more in https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/ .
    The 'LinhSite/wsgi.py': An Entry-point for WSGI-compatible web servers to serve my project. Read more in https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/ .
        (But, I did't know asgi and wsgi before... Don't worry, I can summary after searching it!
            WSGI (Web Server Gateway Interface)
            WSGI is a standard interface between web servers and web applications designed for synchronous applications. It handles HTTP requests one at a time, meaning it processes one request before moving on to the next. WSGI is suitable for traditional web frameworks like Django and Flask.
            In a Django project, wsgi.py serves as the entry-point for WSGI-compatible web servers to launch the application. The entry-point refers to the initial file or function that starts the web application, allowing the server to communicate with the code.

            ASGI (Asynchronous Server Gateway Interface)
            ASGI is a newer standard that supports both synchronous and asynchronous applications. It enables handling multiple tasks concurrently, such as WebSocket connections or asynchronous HTTP requests, making it ideal for modern applications requiring real-time capabilities.
            In Django, asgi.py is the entry-point for ASGI-compatible web servers, enabling the application to handle advanced features like real-time communication via WebSockets. The entry-point is the file or function that initiates the connection between the server and the application, allowing it to start handling requests.
         )

### Step 2. Verify my Django project works:

    python manage.py runserver

To serve the site on a different port, read more in https://docs.djangoproject.com/en/5.1/ref/django-admin/#django-admin-runserver .

And my result:

    $ python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    September 27, 2024 - 02:25:00
    Django version 5.2.dev20240911160443, using settings 'LinhSite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

Here's my page when visit http://127.0.0.1:8000/ with the web browser:
    Lab_1\Part_1\__ProcessImage\Step2.png

Note that in doc:
    This is a lightweight web server written purely in Python. We can develop things rapidly and easily.
    Compared with production server - such as Apache or Nginx - with more complicated configuration.
    Django provides the web frameworks for development progress, not web servers for production progress.


### Step 3. Create the Polls app (Note that we can put my apps in anywhere on my Python path, but, assume that we will create our poll in the same directory as manage.py).

Now we are in the same directory as manage.py, and run:

    python manage.py startapp polls

Knowledge:

    What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

This is structure:
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py

This directory structure will house the poll application.

### Step 4. Write the first view:

Open polls/views.py:

    from django.http import HttpResponse


    def index(request):
        return HttpResponse("I'm Hoai Linh 20PFIEV3, now I'm at the polls index. I've finished Lab_1 For DRF!")

This is the most basic view possible in Django. To access it in a browser, we need to map it to a URL.
To do this, we need to define a URL configuration, or 'URLconf' for short. These URL configurations are defined inside each Django app, and they are Python files named urls.py.

To define a URLconf for the polls app, create a file polls/urls.py with the following content:

    from django.urls import path

    from . import views

    urlpatterns = [
        path("", views.index, name="index"),
    ]
    
### Step 5. Configure the global URLconf in the LinhSite project to include the URLconf defined in poll urls.
To do this, add an import for django.urls.include in LinhSite/urls.py and insert an include() in the urlpatterns list, so we have:

    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path("polls/", include("polls.urls")),
        path("admin/", admin.site.urls),
    ]

The `include()` function allows referencing other URLconfs.

The path("polls/", include("polls.urls")) tells Django: "Whenever the URL starts with polls/, look for more URL patterns in the polls app's urls.py file."
Inside the polls/urls.py, you can define the specific endpoints for the polls app (e.g., polls/vote, polls/results), and `include()` will forward the requests to those URLs.
Use `include()` when you want to include other URL patterns, but `admin.site.urls` is the only exception to this.

The `path()` function expects at least two arguments: route and view.

For example, routes like `admin/` and `polls/` are associated with different apps, and views are the class or function handling requests for those routes.

=> All of the above processing has ensured we have wired an index view into the URLconf! Check it by running:

    python manage.py runserver

Note that go to http://localhost:8000/polls/ in the browser, not only http://localhost:8000/ :).
The text "I'm Hoai Linh 20PFIEV3, now I'm at the polls index. I've finished Lab_1 For DRF!" should be displayed, which was defined in the index view.

Here's my page:
    Lab_1\Part_1\__ProcessImage\Step5.png

### Summary:
In this part of tutorial, we created a basic Django project, set up a polls app, and configured views and URLs to display the index page.
