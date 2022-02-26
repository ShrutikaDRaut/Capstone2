from statistics import mode
from django.db import models

class Product(models.Model):
    product_Id = models.AutoField(primary_key=True, unique=True)
    product_Name = models.CharField(max_length=100)
    display_Price = models.IntegerField()
    min_Price = models.IntegerField()
    product_Img_url = models.URLField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    product_Detail = models.TextField()
    category_Name = models.CharField(max_length=100)

class Order(models.Model):
    order_Id = models.AutoField(primary_key=True, unique=True)
    orderDetail_Id = models.IntegerField()
    orderActual_Price = models.IntegerField()
    orderFinal_Price = models.IntegerField()
    user_Id = models.CharField(max_length=100)

class OrderDetail(models.Model):
    orderDetail_Id = models.AutoField(primary_key=True, unique=True)
    order_Id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_Id = models.IntegerField()
    product_Qty = models.IntegerField()

class User(models.Model):
    user_Id = models.AutoField(primary_key=True, unique=True)
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)
    address = models.CharField(max_length=100)
