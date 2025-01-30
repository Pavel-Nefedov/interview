from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from product.models import Product
from category.models import Category

def product_list(request):
    category = Category.objects.filter(is_deleted=False)
    product = Product.objects.filter(is_deleted=False)
    paginator = Paginator(product, 10)  # 10 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/products.html', {'page_obj': page_obj, 'category': category})

def product_create(request):
    if request.method == "POST":
        product = Product()
        product.category = request.POST.get("category")
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.save()
    return HttpResponseRedirect("/product")

def product_edit(request, id):
    try:
        category = Category.objects.filter(is_deleted=False)
        product = Product.objects.get(id=id)
        if request.method == "POST":
            product.name = request.POST.get("name")
            product.description = request.POST.get("description")
            product.save()
            return HttpResponseRedirect("/product")
        else:
            return render(request, "product_edit.html", {"product": product, 'category': category})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

def product_delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.is_deleted = True
        product.save()
        return HttpResponseRedirect("/product")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")