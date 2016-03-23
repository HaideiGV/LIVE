from django.forms import ModelForm
from django import forms
from models import ViewAllTypeFields, Links
from django.contrib.auth.models import User


class AllFields(ModelForm):
    class Meta:
        model = ViewAllTypeFields
        fields = ['char_field', 'email_field', 'url_field', 'text']


class NewLink(ModelForm):
    class Meta:
        model = Links
        fields = ['category', 'linkUrl', 'description']


class UserForm(forms.Form):
    username = forms.CharField(max_length=100, label='Your name')
    password = forms.CharField(max_length=100, label='Your password', widget=forms.PasswordInput)
    email = forms.CharField(max_length=100, label='Email', widget=forms.EmailInput)