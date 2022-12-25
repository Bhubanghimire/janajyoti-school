from django import forms
from notice.models import Subscriber

# create a ModelForm
from notice.models import Subscriber
from django.forms import ModelForm


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'
        labels = {
            'email': ''
        }
