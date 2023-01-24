from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    modele = Product
    fields = "__all__"
