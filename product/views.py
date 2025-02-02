from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from product.models import Product
from category.models import Category

def product_list(request):
    categories = Category.objects.filter(is_deleted=False)
    product = Product.objects.filter(is_deleted=False)
    paginator = Paginator(product, 10)  # 10 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/products.html', {'page_obj': page_obj, 'categories': categories})


def product_create(request):
    if request.method == "POST":
        product = Product()
        category_id = request.POST.get("category")  # Получаем ID категории из POST
        product.category = get_object_or_404(Category, id=int(category_id))  # Получаем объект категории
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.save()
        return HttpResponseRedirect("/product")

    return HttpResponseRedirect("/product")


def product_edit(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        categories = Category.objects.all()

        if request.method == "POST":
            category_id = request.POST.get("category")  # Получаем ID категории из POST
            product.category = get_object_or_404(Category, id=int(category_id))  # Устанавливаем категорию
            product.name = request.POST.get("name")
            product.description = request.POST.get("description")
            product.save()
            return HttpResponseRedirect("/product")

        else:
            return render(request, "product_edit.html", {"product": product, 'categories': categories})
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