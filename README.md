#### myproject
1.open Desktop of pc and create a folder named 'django-app'
2. open vs code and from view oopen a new terminal and terminal is in command prompt.
3.python -m venv venv
4..\venv\Scripts\activate
5.pip install django
6.django-admin startproject myproject
7.cd myproject
8.python manage.py runserver

To start a Django app on Windows, follow these steps:

##Step 1: Install Python
Download and install Python from the official website. Ensure that you check the box "Add Python to PATH" during installation.

Verify the installation by opening Command Prompt or PowerShell and running:


python --version
##Step 2: Install Django
Open Command Prompt or PowerShell and create a virtual environment to keep your project dependencies isolated:

##python -m venv myenv
Activate the virtual environment:


##myenv\Scripts\activate
After activation, you'll see (myenv) at the beginning of the terminal prompt.

Install Django:


##pip install django
Step 3: Create a New Django Project
Run the following command to create a new Django project (replace myproject with your desired project name):


##django-admin startproject myproject
Navigate to your project folder:


##cd myproject
Run the development server:


##python manage.py runserver
Access your Django site by opening a browser and going to http://127.0.0.1:8000/.

##Step 4: Create a Django App
Inside your project folder (where manage.py is located), create a new Django app:


##python manage.py startapp myapp
Register the app:

##Open the myproject/settings.py file.
Add 'myapp' to the INSTALLED_APPS list:
python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp', 
    # Add your app here
]


##Step 5: Migrate the Database
Run migrations to set up the initial database:


##python manage.py migrate

##Step 6: Start Building Your App
Now that the app is set up, you can start building models, views, and templates!

By following these steps, you can successfully start a Django app on Windows. 
