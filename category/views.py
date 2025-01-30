from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator

from .models import Category


def category_list(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 10)  # 10 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/categories.html', {'page_obj': page_obj})

def category_create(request):
    if request.method == "POST":
        category = Category()
        category.name = request.POST.get("name")
        category.save()
    return HttpResponseRedirect("/category")


def category_edit(request, id):
    try:
        category = Category.objects.get(id=id)
        if request.method == "POST":
            category.name = request.POST.get("name")
            category.save()
            return HttpResponseRedirect("/category")
        else:
            return render(request, "category_edit.html", {"category": category})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")

def category_delete(request, id):
    try:
        category = Category.objects.get(id=id)
        category.is_deleted = True
        category.save()
        return HttpResponseRedirect("/category")
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
