from django.urls import path
from . import views


app_name = "account"
urlpatterns = [
    path("login", views.UserLogin.as_view(), name="user_login"),
    path("otplogin", views.RegisterView.as_view(), name="user_register"),
    path("checkotp", views.CheckOtpView.as_view(), name="check_otp"),
    path("logout", views.user_Logout, name="user_logout"),
]
