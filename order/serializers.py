from rest_framework import serializers

from .models import Ordering


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ordering
        fields = ('user',)
        