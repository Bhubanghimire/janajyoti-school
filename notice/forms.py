from django import forms
from notice.models import Subscriber

# create a ModelForm
class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = "__all__"

        labels = {
            "email":"",
        }
