"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view
from destination.views import destination_detail_view
from property.views import property_detail_view
from review.views import reviews_index_view
from trip.views import trips_index_view
from login.views import login_index_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('destination/', destination_detail_view, name='destination'),
    path('property/', property_detail_view, name='property'),
    path('reviews/', reviews_index_view, name='reviews'),
    path('trips/', trips_index_view, name='trips'),
    path('login/', login_index_view, name='login'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls),
]
