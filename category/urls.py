from django.urls import path
from .views import category_list, category_edit, category_delete, category_create

urlpatterns = [
    path("", category_list),
    path("create/", category_create),
    path("edit/<int:id>/", category_edit),
    path("delete/<int:id>/", category_delete),
]
