from django.shortcuts import render, redirect
from .models import Category, Product, ProductCharacteristic
from .forms import CategoryForm, ProductForm, ProductCharacteristicForm
from django.core.paginator import Paginator

def category_list(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 10)  # 10 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/category.html', {'page_obj': page_obj})

def product_list(request):
    products = Product.objects.filter(is_deleted=False)
    paginator = Paginator(products, 10)  # 10 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/products.html', {'page_obj': page_obj})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.is_deleted = True
    product.save()
    return redirect('product_list')
