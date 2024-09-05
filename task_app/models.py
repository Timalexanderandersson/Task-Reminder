from django.db import models
from django.contrib.auth.models import User

# task list models
class Taskmodel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listoftask")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
#Task model
class UserTask(models.Model):
    title = models.CharField(max_length=200)
    task_list = models.ForeignKey(
        Taskmodel, on_delete=models.CASCADE, related_name="listofall")
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True) 

    def __str__(self):
        return self.title

#Text input model
class Taskcomment(models.Model):
    task_list = models.ForeignKey(
        Taskmodel, on_delete=models.CASCADE, related_name="taskcomments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="usercomments")
    task_content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Task added by {self.user.username} on {self.task_list.name}'