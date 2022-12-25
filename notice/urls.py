from django.urls import path, include
from notice import views


urlpatterns = [
    path("", views.NoticeListView.as_view(), name="notice"),
    path("<int:pk>/detail", views.NoticeDetailView.as_view(), name="notice_detail"),
    path("subscribers", views.subscriber_form, name="subscriber"),
    ]