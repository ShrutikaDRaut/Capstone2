# Generated by Django 3.2.3 on 2022-03-29 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricenegotiator', '0003_rename_user_id_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='last_Name',
            new_name='last_name',
        ),
    ]
