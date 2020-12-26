from django.db import models
from inventory.models import Stock

#contains suppliers
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=50, unique=True)
    cnpj = models.CharField(max_length=15, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name
