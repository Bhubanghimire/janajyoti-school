from django.urls import path
from administration import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('team/', views.TeamListView.as_view(), name="team"),
    path('gallery/', views.gallery, name="gallery"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('login/', views.LoginView, name="login"),

    path("contact-us", views.contact_us, name="contact_us"),
    path("subscriber/", views.SubscriberCreate, name="subscribe")

]