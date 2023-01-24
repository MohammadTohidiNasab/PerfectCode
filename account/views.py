from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect , reverse
from django.views import View
from .forms import LoginForm, RegisterForm, CheckOtpForm
import ghasedakpack
from random import randint

from .models import Otp, User

SMS = ghasedakpack.Ghasedak('c46caa5b2c07f84a61107112753981354941289a44ea543bbb03d43353ec0182')

# # Create your views here.
# def user_login(request):
#     return render(request, 'account/login.html', {})

class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('phone', 'invalid user data')
        else:
            form.add_error('phone', 'invalid data')
        return render(request, 'account/login.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            randomcode = randint(1000, 9999)
            SMS.verification({'receptor': cd['phone'], 'type': '1', 'template': 'randomCode', 'param1': randomcode})
            Otp.objects.create(phone=cd['phone'], code=randomcode)
            print(randomcode)
            return redirect(reverse('account:check_otp') + f'?phone={cd["phone"]}')
        else:
            form.add_error('phone', 'invalid data')
        return render(request, 'account/register.html', {'form': form})

class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm
        return render(request, 'account/check_Otp.html', {'form': form})

    def post(self, request):
        phone = request.GET.get('phone')
        form = CheckOtpForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], phone=phone).exists():
                user = User.objects.create_user(phone=phone)
                login(request, user)
                return redirect('home:home')
        else:
            form.add_error('phone', 'invalid data')
        return render(request, 'account/check_Otp.html', {'form': form})