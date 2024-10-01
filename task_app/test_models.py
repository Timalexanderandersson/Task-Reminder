from django.test import TestCase
from .models import TaskUser
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, time


class TaskUserTest(TestCase):
    '''
    Models testing.
    '''
    def test_all_models_valid(self):
        user = User.objects.create_user(username='Tim')
        task = TaskUser.objects.create(
            user = user,
            title = 'Clean house',
            description = 'Need to clean house',
            completed = False,
            due_date = datetime(2024, 11, 6),
            time_date = time(12, 40),
        )
        self.assertEqual(task.user, user)
        self.assertEqual(task.title, 'Clean house')
        self.assertEqual(task.description, 'Need to clean house')
        self.assertEqual(task.completed, False)
        self.assertEqual(task.due_date, datetime(2024, 11, 6)),
        self.assertEqual(task.time_date, time(12, 40)),





        