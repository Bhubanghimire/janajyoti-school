from django.shortcuts import render
from  django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from allauth.account.views import LoginView, SignupView

# Create your views here.
def home(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def team(request):
    return render(request, "main/team.html")

def testimonials(request):
    return render(request, "main/testimonial.html")

def gallery(request):
    return render(request, "base.html")

def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        user = authenticate(request,email=email, password=password)
        print(password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            Result="Email password doesnt matched"
            return render(request, 'administration/Login.html', {'results': Result})
    else:
        form = LoginForm()
    return render(request, 'administration/Login.html', {'form': form})