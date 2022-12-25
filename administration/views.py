from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from administration.models import ContactUs, About
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

# Create your views here
class HomeView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


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
        user = authenticate(request, email=email, password=password)
        print(password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            Result = "Email password doesnt matched"
            return render(request, 'administration/Login.html', {'results': Result})
    else:
        form = LoginForm()
    return render(request, 'administration/Login.html', {'form': form})


def contact_us(request):
    if request.method == "POST":
        ContactUs.objects.create(name=request.POST["name"], email=request.POST["email"], subject=request.POST["subject"], message=request.POST["message"])
        return redirect("home")

    return render(request, 'main/contact.html')
