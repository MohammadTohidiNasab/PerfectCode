from rest_framework import serializers
from .models import Product, Comment


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

        def validate_massage(self,value):
            filter_list = ['ناسالم','سیاه','کثیف','اشغال']

            for i in filter_list:
                if i in value:
                    raise serializers.ValidationError('کامنت نا محترمانه')
                    