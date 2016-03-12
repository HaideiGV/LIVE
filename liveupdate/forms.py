from django.forms import ModelForm, forms
from models import ViewAllTypeFields, Update, Links, Category
from django import forms

class AllFields(ModelForm):
    class Meta:
        model = ViewAllTypeFields
        exclude = ['aggregate_field']


class NewLink(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    linkUrl = forms.CharField(max_length=200)
    description = forms.CharField(max_length=500)