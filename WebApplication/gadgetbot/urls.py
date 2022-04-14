from django.contrib import admin
from django.urls import path
from pricenegotiator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('process_order/', views.processOrder, name="process_order"),
    path('thank-you', views.orderCompleted, name="order-completed"),
]
