from django.urls import path
from . import views

urlpatterns = [
    
path('', views.product_list,name='list'),
path("<int:id>", views.product_detail, name="detail"),
path('api/', views.ProductViewSet.as_view),

]
