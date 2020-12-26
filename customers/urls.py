from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('customers/', views.CustomerListView.as_view(), name='customers-list'),
    path('customers/new', views.CustomerCreateView.as_view(), name='new-customer'),
    path('customers/<pk>/edit', views.CustomerUpdateView.as_view(), name='edit-customer'),
    path('customers/<pk>/delete', views.CustomerDeleteView.as_view(), name='delete-customer'),
    path('customers/<name>', views.CustomerView.as_view(), name='customer'),
]