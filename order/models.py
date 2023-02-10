from django.db import models
from account.models import User
# Create your models here.


class Ordering(models.Model):
    user = models.ForeignKey(User,max_length=30,on_delete=models.CASCADE)
    product_names = models.CharField(max_length=20) 
    total_products = models.CharField(max_length=30) 
    transaction_id  = models.IntegerField()
    total_amount = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()