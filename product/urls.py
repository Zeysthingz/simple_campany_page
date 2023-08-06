from django.urls import path, include
from .views import products, product_details

urlpatterns = [
    path('products/', products, name='products'),
    path('products/<int:id>/', product_details, name='product_detail'),
]
