import json
from .models import Product, Customer, OrderItem, Order


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']
    minTotal = 0

    for i in cart:
        # try:
        cartItems += int(cart[i]['quantity'])

        product = Product.objects.get(product_Id=i)
        total = float(product.display_Price.replace(',', '')) * \
            float(cart[i]['quantity'])
        order['get_cart_total'] += total

        order['get_cart_items'] += int(cart[i]['quantity'])

        minTotal += float(product.min_Price)

        item = {
            'id': product.product_Id,
            'product': {
                'id': product.product_Id,
                'name': product.product_Name,
                'price': product.display_Price,
                'imageURL': product.product_Img_url
            },
            'quantity': cart[i]['quantity'],
            'get_total': total,
        }
        items.append(item)
        # except:
        #     pass
    return {
        'cartItems': cartItems,
        'items': items,
        'order': order,
        'min_price': minTotal,
    }


def guestOrder(request, data):
    first_name = data['form']['first_name']
    last_name = data['form']['last_name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(email=email, )
    customer.first_name = first_name
    customer.last_name = last_name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(product_Id=item['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity'],
        )
    return customer, order
