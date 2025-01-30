from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

