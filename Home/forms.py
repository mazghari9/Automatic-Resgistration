from django import forms
from django.forms import ModelForm
from .models import Emails


class EmailsForm(ModelForm):
    class Meta:
        model = Emails
        fields = ['Email']