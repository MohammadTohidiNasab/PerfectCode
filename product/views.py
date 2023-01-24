from rest_framework import viewsets
from .serializers import ProductSerializer, CommentSerializer
from . models import Product, Comment
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all.order_by('date')
    serializer_class = CommentSerializer
