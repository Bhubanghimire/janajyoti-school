from administration.models import About as ab
from notice.forms import SubscriberForm


def About(request):
    about=ab.objects.all().first()
    form = SubscriberForm()
    return {'about': about, "form": form}