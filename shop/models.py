from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.template.defaultfilters import default, slugify
from shortuuid.django_fields import ShortUUIDField
from taggit.managers import TaggableManager

User = get_user_model()

class Customer(models.Model):
   user = models.OneToOneField(User, verbose_name=_("Customer"), on_delete=models.CASCADE)
   name = models.CharField(_("Name"), max_length=50)
   email = models.EmailField(_("Emal"), max_length=254)
   
   def __str__(self):
       return self.name
    
class Category(models.Model):
   uuid = ShortUUIDField(
		length=10,
		primary_key=True,
		prefix="cid_",
		max_length=20,
	)
   name = models.CharField(_("Name"), max_length=50, unique=True)
   image = models.ImageField(_("Image"), upload_to='uploads/category')
   
   class Meta:
      verbose_name_plural = 'Categories'
		
   def __str__(self):
      return self.name

   def get_category_img(self):
      return mark_safe(f'<img src={self.image} width=50 height=50 />')
   
   def get_absolute_url(self):
      return reverse("shop:category_detail", kwargs={"cid": self.uuid})

class Product(models.Model):
   name        = models.CharField(_("Name"), max_length=50)
   slug        = models.SlugField(_("Slug"), unique=True)
   image       = models.ImageField(_("Image"), upload_to='uploads/product/')
   description = models.TextField(_("Description"))
   price       = models.FloatField(_("Price"))
   discount    = models.IntegerField(_("Discount %"), null=True, blank=True)
   in_stock    = models.BooleanField(_("in Stock ?"), default=False)
   is_degital  = models.BooleanField(_("Digital"), default=False)
   featured    = models.BooleanField(_("Featured"), default=False)
   created_At  = models.DateTimeField(_("Created"), auto_now_add=True)
   updated_At  = models.DateTimeField(_("Updated"), auto_now=True)
   category    = models.ForeignKey("Category", verbose_name=_("Category"), on_delete=models.CASCADE, null=True)

   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.name)
      return super().save(*args, **kwargs)
   
   def __str__(self):
       return self.name
   
   def get_absolute_url(self):
      return reverse("shop:product_details", kwargs={"slug": self.slug})
   
   def get_product_price(self):
      if self.discount and int(self.discount) > 0:
         price = self.price - ((self.discount * self.price) / 100)
         return price
      return self.price
   
class Collection(models.Model):
   title       = models.CharField(_("Title"), max_length=50)
   deadline    = models.DateTimeField(_("Deadline"), null=True)
   is_active   = models.BooleanField(_("Active"), default=False)
   product     = models.ManyToManyField("Product", verbose_name=_("Item"))
   image       = models.ImageField(_("Background Image"), upload_to='uploads/collection', null=True)
   
   def __str__(self):
      return self.title
   
   def get_absolute_url(self):
      return reverse("model_detail", kwargs={"pk": self.pk})
   

class Order(models.Model):
   customer       = models.ForeignKey("Customer", verbose_name=_("customer"), on_delete=models.SET_NULL, null=True)
   is_completed   = models.BooleanField(_("Status"), default=False)
   date_ordered   = models.DateTimeField(_("CreatedAt"), auto_now_add=True)
   transaction_id  = ShortUUIDField(
		length=10,
		primary_key=True,
		prefix="transaction_",
		max_length=30,
	)
   
   def __str__(self):
       return self.transaction_id
    
   @property
   def get_cart_total(self):
      orderitems = self.orderitem_set.all()
      total = sum([item.total_price for item in orderitems])
      return total
   
   @property
   def get_cart_items(self):
      orderitems = self.orderitem_set.all()
      total = sum([item.quantity for item in orderitems])
      return total
   
class OrderItem(models.Model):
   order       = models.ForeignKey("Order", verbose_name=_("Order"), on_delete=models.CASCADE)
   product     = models.ForeignKey("Product", verbose_name=_("Product"), on_delete=models.CASCADE) 
   quantity    = models.IntegerField(_("Quantity"), default=1)
   date_added  = models.DateTimeField(_("Date Added"), auto_now_add=True)
   
   def __str__(self):
      return f"order {self.order.transaction_id} : {self.id}"
   
   @property
   def total_price(self):
      return self.product.price * self.quantity

class ShippingAddress(models.Model):
   customer    = models.ForeignKey("Customer", verbose_name=_("Customer"), on_delete=models.CASCADE)
   order       = models.ForeignKey("Order", verbose_name=_("Order"), on_delete=models.CASCADE)
   address     = models.CharField(_("Address"), max_length=50, null=True)
   state       = models.CharField(_("State"), max_length=50, null=True)
   city        = models.CharField(_("City"), max_length=50, null=True)
   zipcode     = models.CharField(_("Zip Code"), max_length=50, null=True)
   date_added  = models.DateTimeField(_("Created At"), auto_now_add=True)
   
   def __str__(self):
      return self.address
   
class Cart(models.Model):
   total = models.DecimalField(_("Total"), max_digits=5, decimal_places=2)
   quantity = models.IntegerField(_("Qty"))
   user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
   
class CartItem(models.Model):
   cart = models.ForeignKey("Cart", verbose_name=_("Cart"), on_delete=models.CASCADE)
   product = models.ForeignKey("Product", verbose_name=_("Product"), on_delete=models.CASCADE)
   product_qty = models.IntegerField(_("Qty"), default=0)
   user = models.OneToOneField(User, verbose_name=_(""), on_delete=models.CASCADE)