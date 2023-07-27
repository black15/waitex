from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

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
   context['price'] = product.get_product_price()
   context['product'] = product
   return render(request, 'shop/product/product.html', context)

def category_detail(request, cid):
   context 	= {}
   category = Category.objects.get(uuid=cid)
   products = Product.objects.filter(category=category)
   
   context['products'] = products
   return render(request, 'shop/category_products.html', context)

def cart(request):
   context = {}
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created = Order.objects.get_or_create(customer=customer, is_completed=False)
      items = order.orderitem_set.all()
   else:
      items = []
      order = {'get_cart_total': 0, 'get_cart_items': 0}
      
   context['items'] = items
   context['order'] = order
   return render(request, 'shop/cart/index.html', context)

def product_category_json(request):
   products    = list(Product.objects.values())
   categories  = list(Category.objects.values())
   data = [products, categories]
   return JsonResponse(data,safe=False)

def add_to_cart(request, product, qty):
   item = Product.objects.get(pk=product) 
   cart_obj = Cart.objects.get(user=request.user)
   CartItem.objects.create(cart=cart_obj, product=item, product_qty=qty)
   
def add_item(request):
   data           = json.loads(request.body)
   product_slug   = data['product_slug']
   action         = data['action']
   print(product_slug)
   return JsonResponse('item was added', safe=False)