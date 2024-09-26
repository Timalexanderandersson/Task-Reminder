from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User
from .models import TaskUser

class PostUser(forms.ModelForm):
    class Meta:
        model = TaskUser
        fields = ['title']
