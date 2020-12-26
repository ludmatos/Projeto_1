from django import forms
from django.forms import formset_factory
from .models import (
    Customer
)
from transactions.models import PurchaseBill
from inventory.models import Stock


# form used for customer
class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '11', 'title' : 'Integer'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '11', 'title' : 'Numbers only'})
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address', 'email', 'cpf']
        widgets = {
            'address' : forms.Textarea(
                attrs = {
                    'class' : 'textinput form-control',
                    'rows'  : '3'
                }
            )
        }


# form used to select a customer
class SelectCustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.filter(is_deleted=False)
        self.fields['customer'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = PurchaseBill
        fields = ['customer']

