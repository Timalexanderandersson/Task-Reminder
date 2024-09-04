from django import forms
from .models import UserTask
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

class PostForm(forms.ModelForm):
    class Meta:
        model = UserTask
        fields = ['title','task_list','description','completed','due_date']

