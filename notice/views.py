from django.shortcuts import render, redirect
from notice.forms import SubscriberForm


# Create your views here.
def notice(request):
    return render(request, "main/notice.html")

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