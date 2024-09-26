from django.db import models
from django.contrib.auth.models import User

#Model for adding a task
class UserTask(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listoftask")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    time_date = models.TimeField()

    def __str__(self):
        return self.title
