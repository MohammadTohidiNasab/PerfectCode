from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    modele = Category
    fields = "__all__"
