from django.db import models
from account.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from product.models import Product
# Create your models here.


class Ordering(models.Model):
    user = models.ForeignKey(User, max_length=30, on_delete=models.CASCADE)
    product_names = models.CharField(max_length=20)
    total_products = models.IntegerField()
    transaction_id = models.IntegerField()
    total_amount = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_names


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(90)]
    )
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code



class OrderItem(models.Model):
    order = models.ForeignKey(Ordering, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity