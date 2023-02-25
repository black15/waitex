from django.shortcuts import render
from .models import *

def home(request):
	context = {}
	categories = Category.objects.all()
	
	context['categories'] = categories
	return render(request, 'shop/index.html', context)

def category_detail(request, cid):
   context 	= {}
   category = Category.objects.get(uuid=cid)
   products = Product.objects.filter(category=category)
   
   context['products'] = products
   return render(request, 'shop/category_products.html', context)