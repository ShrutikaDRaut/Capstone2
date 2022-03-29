from django.db import models


class Product(models.Model):
    product_Id = models.AutoField(primary_key=True, unique=True)
    product_Name = models.CharField(max_length=100)
    display_Price = models.CharField(max_length=10)
    min_Price = models.CharField(max_length=10)
    product_Img_url = models.URLField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    product_Detail = models.TextField()
    category_Name = models.CharField(max_length=100)

    def __str__(self):
        """Model obj str representation"""
        return str(self.product_Name)


class Customer(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=75)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, unique=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order_actual_price = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    order_final_price = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.order_id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    order_item_Id = models.AutoField(primary_key=True, unique=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = float(self.product.display_Price) * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False, default="")
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)
