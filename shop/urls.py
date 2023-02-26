from django.contrib import admin
from django.urls import path, include

from .views import home, category_detail, product_details

app_name = 'shop'

urlpatterns = [
	path("", home, name="home"),
	path("product/<slug:slug>", product_details, name="product_details"),
	path("category/<str:cid>", category_detail, name="category_detail"),
]
