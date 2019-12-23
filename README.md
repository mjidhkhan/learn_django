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
