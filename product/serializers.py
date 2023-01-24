from rest_framework import serializers
from .models import Product, Comment

class ProductSerializer(serializers.ModelSerializer):
    modele = Product
    fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    modele = Comment
    fields = "__all__"