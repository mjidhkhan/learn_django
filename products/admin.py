from django.contrib import admin

# Register your models here.
# Relative import.
from .models import Products
admin.site.register(Products) 