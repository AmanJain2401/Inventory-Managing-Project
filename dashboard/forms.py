from dataclasses import field
from pyexpat import model
from django import forms
from .models import product,order

class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields=['name','quantity','category']
    
class orderForm(forms.ModelForm):
    class Meta:
        model = order
        fields=['product','order_quantity']
