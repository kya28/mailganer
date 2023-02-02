import sys
from datetime import date
from config.celery_app import app
from django.core.mail import send_mail
from django.db.models import signals

from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'We congratulations you a happy birthday!',
            'Dear {}, CONGRATULATIONS!!!'.format(contact.first_name),
            'ks-sh@internet.ru',
            [contact.email],
            fail_silently=False,
        )
