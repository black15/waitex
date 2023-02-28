from django.shortcuts import render
from .models import *

def home(request):
	context = {}
	categories  = Category.objects.all()
	products    = Product.objects.all() 
	collections = Collection.objects.filter(is_active=True)
    
	context['products']     = products
	context['categories']   = categories
	context['collections']  = collections
	return render(request, 'shop/index.html', context)

def product_details(request, slug):
   context 	= {}
   product = Product.objects.get(slug=slug)
   
   context['product'] = product
   return render(request, 'shop/product/product.html', context)

def category_detail(request, cid):
   context 	= {}
   category = Category.objects.get(uuid=cid)
   products = Product.objects.filter(category=category)
   
   context['products'] = products
   return render(request, 'shop/category_products.html', context)