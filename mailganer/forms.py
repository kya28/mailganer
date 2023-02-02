from django.forms import extras
from mailganer.models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta(object):
        model = Contact
        fields = '__all__'
        widgets = {
            'birthday': extras.SelectDateWidget(years=range(1940, 2014))
        }

