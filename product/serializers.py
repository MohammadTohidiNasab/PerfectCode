from rest_framework import serializers
from .models import Product, Comment


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')



class CommentSerializer(serializers.ModelSerializer):
    modele = Comment
    fields = "__all__"