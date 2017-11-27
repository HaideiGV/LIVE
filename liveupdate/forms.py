from django.forms import ModelForm
from django import forms
from .models import Contacts, Links


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['subject', 'email', 'text']


class NewLink(ModelForm):
    class Meta:
        model = Links
        fields = ['linkUrl', 'description']


class UserForm(forms.Form):
    username = forms.CharField(max_length=100, label='Your name')
    password = forms.CharField(max_length=100, label='Your password', widget=forms.PasswordInput)
    email = forms.CharField(max_length=100, label='Email', widget=forms.EmailInput)
