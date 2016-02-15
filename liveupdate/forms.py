from django.forms import ModelForm
from models import ViewAllTypeFields, Update

class AllFields(ModelForm):
    class Meta:
        model = ViewAllTypeFields
        exclude = ['aggregate_field']


class NewPost(ModelForm):
    class Meta:
        model = Update
        fields = ['text']