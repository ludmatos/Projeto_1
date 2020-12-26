from django import forms
from django.forms import formset_factory
from .models import (
    Supplier
)
from transactions.models import PurchaseBill
from inventory.models import Stock


# form used for supplier
class SupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '11', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['cnpj'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '15', 'title' : 'Numbers only'})
    class Meta:
        model = Supplier
        fields = ['name', 'phone', 'address', 'email', 'cnpj']
        widgets = {
            'address' : forms.Textarea(
                attrs = {
                    'class' : 'textinput form-control',
                    'rows'  : '3'
                }
            )
        }

# form used to select a supplier
class SelectSupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].queryset = Supplier.objects.filter(is_deleted=False)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = PurchaseBill
        fields = ['supplier']