from django.urls import path, include
from notice import views


urlpatterns = [
    path("", views.notice, name="notice")
    ]