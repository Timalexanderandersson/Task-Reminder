from django import forms
from .models import UserTask, Taskmodel, Taskcomment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class PostForm(forms.ModelForm):
    class Meta:
        model = Taskmodel
        fields = ['user', 'name',]
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        
