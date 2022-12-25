from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from administration.models import ContactUs, About, Staff, Testimonials
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from notice.forms import SubscriberForm
from django.views.generic import ListView, CreateView
from notice.models import Notice, Subscriber
from django.views.decorators.csrf import csrf_exempt


# Create your views here
class HomeView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["staffs"] = Staff.objects.filter(active=True)
        context["testimonials"] = Testimonials.objects.all()
        return context


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


class AboutView(TemplateView):

    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["staffs"] = Staff.objects.filter(active=True)
        return context


def contact(request):
    return render(request, "main/contact.html")


class TeamListView(ListView):
    model = Staff
    context_object_name = "staff_list"
    template_name =  "main/team.html"


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
