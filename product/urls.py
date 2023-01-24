from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('detail/', views.product_detail),
    path('api', views.ProductViewSet.as_view),
]
