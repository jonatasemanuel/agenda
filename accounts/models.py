from django.db import models
from contacts.models import Contact, Status
from django import forms


# Create your models here.
class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('show',)