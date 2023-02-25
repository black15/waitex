from django.contrib import admin
from django.urls import path, include

from .views import home, category_detail

app_name = 'shop'

urlpatterns = [
	path("", home, name="home"),
	path("category/<str:cid>", category_detail, name="category_detail"),
]
