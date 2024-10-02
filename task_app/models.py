from django.db import models
from django.contrib.auth.models import User

#Task model
class TaskUser(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    time_date = models.TimeField(blank=False)


    def __str__(self):
        return self.title
#Contact form
class FormContact(models.Model):
    name = models.CharField(max_length=70, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name