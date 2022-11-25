from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from administration.models import ContactUs, About
from django.shortcuts import render
from notice.forms import SubscriberForm
from django.views.generic import ListView, CreateView
from notice.models import Notice, Subscriber


# Create your views here.
# class SubscriberCreate(CreateView):
#     model = Subscriber
#     template_name = "main/index.html"
#     form_class = SubscriberForm
#     success_url = "/"
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def SubscriberCreate(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect(request.META['HTTP_REFERER'])

    return redirect(request.META['HTTP_REFERER'])


def home(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def contact(request):
    about = About.objects.all().first()
    print(about)
    return render(request, "main/contact.html", {"about": about})


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
        ContactUs.objects.create(name=request.POST["name"], email=request.POST["email"],
                                 subject=request.POST["subject"], message=request.POST["message"])
        return redirect("home")

    return render(request, 'main/contact.html')
