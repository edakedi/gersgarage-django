# gersgarage-django

### Installing 
First, you need to install virtualenv for Python 3.7. You can find installation instructions  for your operating system

To activate your environment:
```
source venv/bin/activate
```
### Installing Packages
```
Django==3.2.6
django-autoslug==1.9.8
psycopg2==2.9.1
psycopg2-binary==2.9.1
```

### Running

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


********
Dont forget to configure your database from gersgarage/settings.py
********
