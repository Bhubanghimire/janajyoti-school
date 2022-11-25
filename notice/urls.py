from django.urls import path, include
from notice import views


urlpatterns = [
    path("", views.NoticeListView.as_view(), name="notice"),
    # path("subscriber/", views.SubscriberCreate.as_view(), name="subscribe")
    ]
