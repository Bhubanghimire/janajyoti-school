from django.shortcuts import render, redirect
from notice.forms import SubscriberForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from notice.models import Notice

# Create your views here.
class NoticeListView(ListView):
    model = Notice
    template_name = "main/notice.html"
    context_object_name = "topics"
    paginate_by = 10

class NoticeDetailView(DetailView):
    model = Notice
    template_name = "main/noticedetail.html"
    context_object_name = "notice_object"

def subscriber_form(request):
    context = {}
    form = SubscriberForm(request.POST or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect("home")

    context['form'] = form
    return render(request, "main/index.html", context)