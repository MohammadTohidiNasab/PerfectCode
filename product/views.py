from rest_framework import viewsets
from .serializers import ProductSerializer
from . models import Product
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

# Create your views here.

#api
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'stock','price']



#django

#list view
def product_list(request):
    food_list = Product.objects.all()
    context= {
        "product" : product_list
              }
    
    return render (request,'shop.html',context)


#detail view
def product_detail(requste,id):
    food = Product.objects.get(id = id)
    
    context = {
        'product': product_detail
    }
    
    return render(requste,'detail.html',context)

