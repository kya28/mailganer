from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView

from mailganer.forms import ContactForm
from mailganer.models import Contact
from .service import send
from .tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'mailganer/index.html'

    def form_valid(self, form):
        form.save()
        #send(form.instance.email)
        send_spam_email.delay(form.instance.email)
        return super(ContactView, self).form_valid(form)
