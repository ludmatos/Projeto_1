from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View, 
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import (  
    Customer,
    Pet
)
from transactions.models import PurchaseBill
from .forms import (
    CustomerForm,
    SelectCustomerForm
)
from inventory.models import Stock


# shows a lists of all customers
class CustomerListView(ListView):
    model = Customer
    template_name = "customers_list.html"
    queryset = Customer.objects.filter(is_deleted=False)
    paginate_by = 15


# used to add a new customer
class CustomerCreateView(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = '/customers/customers'
    success_message = "Customer has been created successfully"
    template_name = "edit_customer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Customer'
        context["savebtn"] = 'Add Customer'
        return context     


# used to update a customer's info
class CustomerUpdateView(SuccessMessageMixin, UpdateView):
    model = Customer
    #form_class = SelectCustomerForm
    form_class = CustomerForm
    success_url = '/customers/customers'
    success_message = "Customer details has been updated successfully"
    template_name = "edit_customer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Customer'
        context["savebtn"] = 'Save Changes'
        context["delbtn"] = 'Delete Customer'
        return context


# used to delete a customer
class CustomerDeleteView(View):
    template_name = "delete_customer.html"
    success_message = "Customer has been deleted successfully"

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, self.template_name, {'object' : customer})

    def post(self, request, pk):  
        customer = get_object_or_404(Customer, pk=pk)
        customer.is_deleted = True
        customer.save()                                               
        messages.success(request, self.success_message)
        return redirect('customers-list')


# used to view a customer's profile
class CustomerView(View):
    def get(self, request, name):
        customerobj = get_object_or_404(Customer, name=name)
        bill_list = PurchaseBill.objects.filter(customer=customerobj)
        page = request.GET.get('page', 1)
        paginator = Paginator(bill_list, 10)
        try:
            bills = paginator.page(page)
        except PageNotAnInteger:
            bills = paginator.page(1)
        except EmptyPage:
            bills = paginator.page(paginator.num_pages)
        context = {
            'customer'  : customerobj,
            'bills'     : bills
        }
        return render(request, 'customers/customer.html', context)

