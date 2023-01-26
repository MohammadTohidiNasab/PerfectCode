from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', views.ProductViewSet)




urlpatterns = [
    
path('', views.product_list,name='list'),
path("<int:id>", views.product_detail, name="detail"),
path('api/', include(router.urls)),

]
