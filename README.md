# How to django 
### Check virtualenv installed 

```shell
$ virtualenv
```

### Create virtual enviornment with python3

```shell
$ virtualenv -p python3 .
```

### Activate virtual enviornment 

```shell
$ source bin/activate
```

### Deactivate virtual enviornment
```shell
$ deactivate
```


## Install django

```shell
$ pip install django
```


### Check what is installed 
```shell
$ pip freeze
```

## Create direvtory src
```shell
$ mkdir src 
```
## Create a django Project
```shell
$ django-admin  startproject mysite
```
 
### Do required migrations 
```shell
$ python manage.py migrate

```
### Create superuser(admin for the site) [mhk 12345678]

```shell
$ python manage.py createsuperuser
```
## Create First app component
```shell
$ python manage.py startapp products
```
### Write following code in  products/model.py
```python
class Products(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
```
### Run following commands for products [PCMD]
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

Add following line in products/model.py

```python
summary     = models.TextField()
``` 
run products command [PCMD] you will see following message
```shell
You are trying to add a non-nullable field 'summary' to products without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
 ```
 select 2 and add youseld some default as we write 
 ***'It is cool'*** as shown below
 ```python
 summary     = models.TextField(default='It is cool')
 ```

 First run following command
 ```shell
 $ python manage.py makemigrations
 ```
 You will see following message
 ```shell
 Migrations for 'products':
  products/migrations/0002_products_summary.py
    - Add field summary to products
```

Then run fllowing command 
```shell
$ python manage.py migrate
```
On success you will see message like give below
```shell
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, products, sessions
Running migrations:
  Applying products.0002_products_summary... OK
```

Add Product model to admin 
Open admin.py from migrations
```python 
# Register your models here.
# Relative import.
from .models import Products
admin.site.register(Products) 
```
refresh local websit and you will see Products area.

Using manage.py shell to runn project
rumm following command 
```shell
$ python manage.py shell
```
you will see somtninh like shown below
```shell
Python 3.7.4 (default, Sep  7 2019, 18:31:37)
[Clang 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```
note it is an Interactive console where now you can bring your whole project to shell.

```shell
>>> from products.models import Products
>>> Products.objects.all()
<QuerySet [<Products: Products object (1)>]>
```
as we have one product in database it is showing one object.

few commands
```shell
>>> Products.objects.create(title='New Product 2', description='new product two', price='20', summary='another product')
```


# The integration of Tailwind CSS framework with Django a.k.a. Django + Tailwind = ❤

Author: Tim Kamanin
## Quick start
Install the python package django-tailwind from pip
```shell
$ pip install django-tailwind
```
Alternatively, you can download or clone this repo and run pip install -e ..

Add tailwind to INSTALLED_APPS in settings.py

Create a tailwind-compatible Django-app, I like to call it theme:
```shell
$ python manage.py tailwind init theme
```
Add your newly created theme app to INSTALLED_APPS in settings.py

In settings.py, register tailwind app by adding the following string:
```python
TAILWIND_APP_NAME = 'theme'
```
Run a command to install all necessary dependencies for tailwind css:

```shell
python manage.py tailwind install
```
Now, go and start tailwind in dev mode:
```shell
python manage.py tailwind start
```
Django Tailwind comes with a simple base.html template that can be found under yourtailwindappname/templates/base.html. You can always extend it or delete it if you have own layout.

If you're not using base.html template provided with Django Tailwind, add styles.min.css to your own base.html template file:

<link
  rel="stylesheet"
  href="{% static 'css/styles.min.css' %}"
  type="text/css"
/>
You should now be able to use Tailwind CSS classes in your html.

To build a production version of CSS run:
```shell
python manage.py tailwind build.
```
NPM executable path configuration
Sometimes (especially on Windows), Python executable can't find NPM installed in the system. In this case, you need to set NPM executable path in settings.py file manually:
```
NPM_BIN_PATH = '/usr/local/bin/npm'
```
Please note that NPM path of your system may be different. Try to run which npm in your command line to get the path.
