from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User
from .models import TaskUser
from django.contrib.auth.forms import UserCreationForm
#Posting Tasks
class PostUser(forms.ModelForm):
    class Meta:
        model = TaskUser
        fields = ['title','description','completed','due_date','time_date']
        widgets = {
            'due_date': forms.SelectDateWidget(attrs={'type':'date'}),
            'time_date':forms.TimeInput(attrs={'type':'time'})
        }
#Signing up account
class SigningUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']