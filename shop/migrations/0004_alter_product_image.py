# Generated by Django 4.1.7 on 2023-02-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='uploads/product/', verbose_name='Image'),
        ),
    ]
