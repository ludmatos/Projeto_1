from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=0)
    category_tag = models.CharField(max_length=20, null=True)
    NCM = models.IntegerField(null=False, default=0)
    bar_code = models.IntegerField(unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name