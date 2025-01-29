from django.urls import path
from .views import category_list, product_list, delete_product

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('products/', product_list, name='product_list'),
    path('products/delete/<int:product_id>/', delete_product, name='delete_product'),
]
