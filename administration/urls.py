from django.urls import path
from administration import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('team/', views.team, name="team"),
    path('gallery/', views.gallery, name="gallery"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('login/', views.LoginView, name="login"),

    path("contact-us", views.contact_us, name="contact_us"),

]