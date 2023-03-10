# Generated by Django 4.1.7 on 2023-02-24 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shop.models
import shortuuid.django_fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=20, prefix='cid_', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('image', models.ImageField(upload_to='uploads/category', verbose_name='Image')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Emal')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('date_ordered', models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt')),
                ('tansaction_id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=30, prefix='transaction_', primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.customer', verbose_name='customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='Address')),
                ('state', models.CharField(max_length=50, null=True, verbose_name='State')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='City')),
                ('zipcode', models.CharField(max_length=50, null=True, verbose_name='Zip Code')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='Customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('image', models.ImageField(upload_to='uploads/product', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Discount %')),
                ('in_stock', models.BooleanField(default=False, verbose_name='in Stock ?')),
                ('is_degital', models.BooleanField(default=False, verbose_name='Digital')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured')),
                ('created_At', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_At', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Product')),
            ],
        ),
    ]
