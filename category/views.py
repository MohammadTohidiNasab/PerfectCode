from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]


