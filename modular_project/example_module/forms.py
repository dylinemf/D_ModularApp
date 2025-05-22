from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'barcode', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Agua'}),
            'barcode': forms.TextInput(attrs={'placeholder': 'ABC-abc-1234'}),
            'price': forms.NumberInput(attrs={'placeholder': '3500'}),
            'stock': forms.NumberInput(attrs={'placeholder': '20'}),
        }
