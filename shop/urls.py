from django.contrib import admin
from django.urls import path, include

from .views import home

app_name = 'shop'

urlpatterns = [
	 path("index", home, name="home"),
]
