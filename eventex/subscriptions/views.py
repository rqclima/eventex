from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateMixin
from eventex.subscriptions.models import Subscription


class EmailCreateView(EmailCreateMixin, CreateView):
    def form_valid(self, form):
        response = super().form_valid(form)
        self.send_mail()
        return response


new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de inscrição')


# TODO Usar DetailView, ver M4A11, 23min
# DetailView

def detail(request, hash_id):
    try:
        subscription = Subscription.objects.get(hash_id=hash_id)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})
