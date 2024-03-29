from rest_framework import serializers
from .models import Ordering


class OrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering
        fields = "user"
