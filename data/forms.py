from django import forms
from django.forms import ModelForm
from .models import *

class OrderFrom(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'custumer' : forms.Select(attrs={'class' : 'form-control'}),
            'product' : forms.Select(attrs={'class' : 'form-control'}),
            'status' : forms.Select(attrs={'class' : 'form-control'}),
        }
        labels = {
            'custumer':'Konsumen',
            'product':'Produk',
            'status':'Status Order',
        }
        
class CustumerForm(ModelForm):
    class Meta:
        model = Custumer
        fields = '__all__'
        widgets = {
            # 'name'  : forms.Select(attrs={'class' : 'form-control'}),
            # 'phone' : forms.Select(attrs={'class' : 'form-control'}),
        #     'email' : forms.Select(attrs={'class' : 'form-control'}),
        }
        labels = {
        #     'name':'Nama',
        #     'phone':'No hp',
        #     'email':'Akun Email',
        }
            