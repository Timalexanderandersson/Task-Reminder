from django.contrib import admin
from .models import TaskUser, FormContact
'Admin for TaskUser.'
admin.site.register(TaskUser)

'Admin for FormContact'
admin.site.register(FormContact)