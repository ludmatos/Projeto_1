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

from .models import Supplier
from transactions.models import PurchaseBill

from .forms import (
    SelectSupplierForm,     
    SupplierForm
)

from inventory.models import Stock

# shows a lists of all suppliers
class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers_list.html"
    queryset = Supplier.objects.filter(is_deleted=False)
    paginate_by = 10


# used to add a new supplier
class SupplierCreateView(SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    success_url = '/suppliers/suppliers'
    success_message = "Supplier has been created successfully"
    template_name = "edit_supplier.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Supplier'
        context["savebtn"] = 'Add Supplier'
        return context     


# used to update a supplier's info
class SupplierUpdateView(SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    success_url = '/suppliers/suppliers'
    success_message = "Supplier details has been updated successfully"
    template_name = "edit_supplier.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Supplier'
        context["savebtn"] = 'Save Changes'
        context["delbtn"] = 'Delete Supplier'
        return context


# used to delete a supplier
class SupplierDeleteView(View):
    template_name = "delete_supplier.html"
    success_message = "Supplier has been deleted successfully"

    def get(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        return render(request, self.template_name, {'object' : supplier})

    def post(self, request, pk):  
        supplier = get_object_or_404(Supplier, pk=pk)
        supplier.is_deleted = True
        supplier.save()                                               
        messages.success(request, self.success_message)
        return redirect('suppliers-list')


# used to view a supplier's profile
class SupplierView(View):
    def get(self, request, name):
        supplierobj = get_object_or_404(Supplier, name=name)
        bill_list = PurchaseBill.objects.filter(supplier=supplierobj)
        page = request.GET.get('page', 1)
        paginator = Paginator(bill_list, 10)
        try:
            bills = paginator.page(page)
        except PageNotAnInteger:
            bills = paginator.page(1)
        except EmptyPage:
            bills = paginator.page(paginator.num_pages)
        context = {
            'supplier'  : supplierobj,
            'bills'     : bills
        }
        return render(request, 'suppliers/supplier.html', context)
