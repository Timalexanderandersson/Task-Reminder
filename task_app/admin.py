from django.contrib import admin
from .models import Taskmodel, UserTask, Taskcomment

# 
admin.site.register(Taskmodel)
admin.site.register(UserTask)
admin.site.register(Taskcomment)

