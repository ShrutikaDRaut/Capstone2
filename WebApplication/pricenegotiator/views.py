import os
import json
import datetime
import pandas as pd
from django.shortcuts import render
from pathlib import Path
from .models import *
from .utils import cookieCart, guestOrder
from django.http import JsonResponse

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    total_products = Product.objects.all()
    if len(total_products) == 0:
        products = pd.read_csv(os.path.join(BASE_DIR, 'product.csv'))
        for product in range(len(products)):
            item = Product.objects.create()
            item.product_Name = products.iloc[product, 1]
            item.display_Price = products.iloc[product, 2]
            item.min_Price = products.iloc[product, 3]
            item.model = products.iloc[product, 4]
            item.brand = products.iloc[product, 5]
            item.product_Detail = products.iloc[product, 6]
            item.category_Name = products.iloc[product, 7]
            item.product_Img_url = products.iloc[product, 8]
            item.save()
    all_products = Product.objects.all()

    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']

    context = {'products': all_products, 'cartItems': cartItems}
    return render(request, 'index.html', context)


def product_detail(request, product_id: int):
    product = Product.objects.get(product_Id=product_id)
    productdetail = json.loads(
        '"' + product.product_Detail.replace("'", " ").replace(" ,", ",") +
        '"')

    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    items = cookieData['items']

    cartQuantity = 1
    if len(items) != 0:
        for item in items:
            if item['id'] == product_id:
                cartQuantity = item['quantity']
    else:
        cartQuantity = 1
    print(cartQuantity)
    context = {
        'product': product,
        'productDetail': productdetail,
        'cartItems': cartItems,
        'cartQuantity': cartQuantity
    }
    return render(request, 'product.html', context)


def cart(request):
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    items = cookieData['items']
    order = cookieData['order']

    context = {
        'cartItems': cartItems,
        'items': items,
        'order': order,
        "wholeCart": cookieData
    }
    return render(request, 'cart.html', context)


def checkout(request):
    cookieData = cookieCart(request)

    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']

    tax = order['get_cart_total'] * 0.13
    total = order[
        'get_cart_total'] + order['get_cart_total'] * 0.13 - 120.00 + 5
    priceValues = {
        'subtotal': order['get_cart_total'],
        'tax': f'{tax:.2f}',
        'discount': 120.00,
        'total': f'{total:.2f}'
    }
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'priceValues': priceValues
    }
    return render(request, 'checkout.html', context)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer, order = guestOrder(request, data)

    subtotal = float(data['form']['subtotal'])
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    order.order_actual_price = subtotal
    order.order_final_price = total
    order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        country=data['shipping']['country'],
    )

    return JsonResponse('Payment completed!', safe=False)


def orderCompleted(request):
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']

    context = {'cartItems': cartItems}
    return render(request, 'thankyou.html', context)
