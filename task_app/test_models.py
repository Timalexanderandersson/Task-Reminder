from django.test import TestCase
from .models import TaskUser, FormContact
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, time


class TaskUserTest(TestCase):
    '''
    Models testing if all valid.
    '''
    def test_model_taskuser_valid(self):
        user = User.objects.create(username='Tim')
        task = TaskUser.objects.create(
            user = user,
            title = 'Clean house',
            description = 'Need to clean house',
            completed = False,
            due_date = datetime(2024,12,16),
            time_date = time(10,30),
        )
        self.assertEqual(task.user, user)
        self.assertEqual(task.title, 'Clean house')
        self.assertEqual(task.description, 'Need to clean house')
        self.assertEqual(task.completed, False)
        self.assertEqual(task.due_date, datetime(2024,12,16))
        self.assertEqual(task.time_date, time(10,30))


class FormContactTesting(TestCase):
    '''
    Form testing if all valid.
    '''
    def test_form_contact_is_valid(self):
        form = FormContact.objects.create(
            name = 'Tim',
            email = 'tim@hotmail.com',
            message = 'hello',
        )
        self.assertEqual(form.name, 'Tim')
        self.assertEqual(form.email, 'tim@hotmail.com')
        self.assertEqual(form.message, 'hello')