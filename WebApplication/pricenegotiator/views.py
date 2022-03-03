from django.shortcuts import render
from pathlib import Path
from .models import Product
import pandas as pd
import os

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
    return render(request, 'index.html', {'products': all_products})
