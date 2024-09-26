from django import forms
from .models import UserTask
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class PostUser(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = ['title','description','completed','due_date','time_date']





        
