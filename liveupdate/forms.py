from django.forms import ModelForm, forms
from models import ViewAllTypeFields, Update, Links, Category
from django import forms

class AllFields(ModelForm):
    class Meta:
        model = ViewAllTypeFields
        fields = ['char_field', 'email_field', 'url_field', 'text']


class NewLink(ModelForm):
    class Meta:
        model = Links
        fields = ['category', 'linkUrl', 'description']
