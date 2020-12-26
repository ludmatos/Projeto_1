from django.db import models


#contains customer table
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=50, unique=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name

#contains pet table
class Pet(models.Model):
    owner_id = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name='customername')
    name = models.CharField(max_length=100)    
    breed = models.CharField(max_length=25, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name
