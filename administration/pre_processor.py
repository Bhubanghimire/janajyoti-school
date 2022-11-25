from notice.forms import SubscriberForm


def processor(request):
    return {
       'form': SubscriberForm,
    }
