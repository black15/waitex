# Generated by Django 4.1.7 on 2023-07-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_cart_rename_status_order_is_completed_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tansaction_id',
            new_name='transaction_id',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity'),
        ),
    ]