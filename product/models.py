from django.db import models
from category.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
