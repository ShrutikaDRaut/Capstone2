# Generated by Django 3.2.3 on 2022-03-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricenegotiator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
