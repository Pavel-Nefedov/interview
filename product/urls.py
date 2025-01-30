from django.urls import path
from .views import product_list, product_create, product_edit, product_delete

urlpatterns = [
    path("", product_list),
    path("create/", product_create),
    path("edit/<int:id>/", product_edit),
    path("delete/<int:id>/", product_delete),
]
