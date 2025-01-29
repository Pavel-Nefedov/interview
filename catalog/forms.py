from django import forms
from .models import Category, Product, ProductCharacteristic

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name']

class ProductCharacteristicForm(forms.ModelForm):
    class Meta:
        model = ProductCharacteristic
        fields = ['product', 'name', 'value']

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('name') or not cleaned_data.get('value'):
            raise forms.ValidationError("Поля не могут быть пустыми.")
