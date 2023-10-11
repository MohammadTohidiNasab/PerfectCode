from django.urls import path
from . import views

urlpatterns = [
    path("request/", views.go_to_gateway_view, name="request"),
    path("verify/", views.callback_gateway_view, name="verify"),
]
