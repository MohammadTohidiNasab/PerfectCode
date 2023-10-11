from rest_framework import viewsets
from .serializers import ProductSerializer, CommentSerializer
from .models import Product, Comment
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Create your views here.


# api
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ["category", "price"]

    search_fields = ["category"]
    ordering_fields = ["price"]

    # permission for authenticated users
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# django


# list view
def product_list(request):
    food_list = Product.objects.all()
    context = {"product": product_list}

    return render(request, "shop.html", context)


# detail view
def product_detail(requste, id):
    food = Product.objects.get(id=id)

    context = {"product": product_detail}

    return render(requste, "detail.html", context)
