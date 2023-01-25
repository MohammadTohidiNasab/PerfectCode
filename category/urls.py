from django.urls import path
from . import views

urlpatterns = [
    
    path('category/<slug:category>',views.CategoryViewSet.as_view,name='category'),

]
