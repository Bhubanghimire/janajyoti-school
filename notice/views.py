from django.shortcuts import render
from notice.forms import SubscriberForm
from django.views.generic import ListView, CreateView
from notice.models import Notice,Subscriber


# Create your views here.
class NoticeListView(ListView):
    model = Notice
    template_name = "main/notice.html"


