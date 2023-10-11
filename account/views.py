from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import LoginForm, RegisterForm, CheckOtpForm
import ghasedakpack
from random import randint
from django.utils.crypto import get_random_string
from .models import Otp, User
from uuid import uuid4

SMS = ghasedakpack.Ghasedak(
    "c46caa5b2c07f84a61107112753981354941289a44ea543bbb03d43353ec0182"
)

# # Create your views here.
# def user_login(request):
#     return render(request, 'account/login.html', {})


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error("username", "invalid user data")
        else:
            form.add_error("username", "invalid data")
        return render(request, "account/login.html", {"form": form})


def user_Logout(request):
    logout(request)
    return redirect("home:home")


class RegisterView(View):
    def get(self, request):
        form = RegisterForm
        return render(request, "account/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            randomcode = randint(1000, 9999)
            SMS.verification(
                {
                    "receptor": cd["phone"],
                    "type": "1",
                    "template": "randomCode",
                    "param1": randomcode,
                }
            )
            token = str(uuid4())
            Otp.objects.create(phone=cd["phone"], code=randomcode, token=token)
            print(randomcode)
            return redirect(reverse("account:check_otp") + f"?token={token}")
        else:
            form.add_error("phone", "invalid data")
        return render(request, "account/register.html", {"form": form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm
        return render(request, "account/check_Otp.html", {"form": form})

    def post(self, request):
        token = request.GET.get("token")
        form = CheckOtpForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd["code"], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(
                    request, user, backend="django.contrib.auth.backends.ModelBackend"
                )
                otp.delete()
                return redirect("home:home")
        else:
            form.add_error("phone", "invalid data")
        return render(request, "account/check_Otp.html", {"form": form})
