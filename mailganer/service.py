from django.core.mail import send_mail


def send(user_email):
    send_mail('You follow for our',
              'congratulations! You follow for our',
              'ks-sh@internet.ru',
              [user_email],
              fail_silently=False,
        )



