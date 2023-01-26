from rest_framework import viewsets
from .serializers import ProductSerializer
from . models import Product

from django.shortcuts import render

# Create your views here.

#api
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer



#django

#listview
def product_list(request):
    food_list = Product.objects.all()
    context= {
        "product" : product_list
              }
    
    return render (request,'shop.html',context)


#detailview
def product_detail(requste,id):
    food = Product.objects.get(id = id)
    
    context = {
        'product': product_detail
    }
    
    return render(requste,'detail.html',context)

