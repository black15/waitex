# Generated by Django 4.1.7 on 2023-02-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_collection_product_collection_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/collection', verbose_name='Background Image'),
        ),
        migrations.AddField(
            model_name='collection',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]
