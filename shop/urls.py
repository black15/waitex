from django.contrib import admin
from django.urls import path, include

from .views import home, cart, category_detail, product_details, product_category_json

app_name = 'shop'

urlpatterns = [
	path("", home, name="home"),
	path("cart", cart, name="cart"),
	path("product/<slug:slug>", product_details, name="product_details"),
	path("category/<str:cid>", category_detail, name="category_detail"),
	path("json-data/", product_category_json, name="product_category_json"),
]
