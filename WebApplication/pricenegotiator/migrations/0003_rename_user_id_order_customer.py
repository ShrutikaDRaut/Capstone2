# Generated by Django 3.2.3 on 2022-03-29 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricenegotiator', '0002_alter_order_date_ordered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='customer',
        ),
    ]
