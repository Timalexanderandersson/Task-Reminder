from django.test import TestCase, Client
from .models import TaskUser, FormContact
from django.contrib.auth.models import User
from django.urls import reverse

class IndexPageTest(TestCase):
    '''
    Testin That index.html/ and when sign in task_edit works.
    '''
    def test_for_index_webpage_valid(self):
        self.client = Client()
        url = reverse('Homepage')
        answer = self.client.get(url)
        self.assertEqual(answer.status_code,200)

    def test_for_task_edit_webpage_valid(self):
        user = User.objects.create_user(username='Tim', password='Monkey123')
        self.client.login(username='Tim', password='Monkey123')
        url = reverse('task-create')
        answer = self.client.get(url)
        self.assertEqual(answer.status_code,200)

class TestSignUp(TestCase):
    '''
    Test if sign up is valid.
    '''
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')
        self.data = {
            'username':'tim',
            'email':'tim@hotmail.com',
            'password1':'wowmonkey1234',
            'password2':'wowmonkey1234'
        }

    def test_sign_up_is_valid(self):
        answer = self.client.post(self.url,self.data)
        self.assertEqual(answer.status_code,302)


    def test_invalid_passwords(self):
        '''
        invalid password test.
        '''
        self.data['password2'] = 'password_wrong2'
        self.data['password1'] = 'password_wrong'

class TestSignIn(TestCase):
    '''
    Test if sign in is valid.
    '''
    def setUp(self):
        
        self.client = Client()
        self.url = reverse('login')
        self.data = {
            'username':'tim',
            'password':'wowmonkey1234',
        }

    def test_sign_in_is_valid(self):
        '''
        sign in and redirected to task-create.
        '''
        user = User.objects.create_user(username='tim', password='Monkey123')
        self.client.login(username='tim', password='Monkey123')
        answer = self.client.post(self.url,self.data)
        self.assertEqual(answer.status_code,302)

    def test_invalid_passwords_sign_in(self):
        '''
        invalid password/username test.
        '''
        self.data['username'] = 'hey'
        self.data['password'] = 'password_wrong'

class SignOutTest(TestCase):
    '''
    Test for sign out redirect to homepage.
    '''
    def setUp(self):
        self.client = Client()
        self.url = reverse('logout')
        self.data = {
            'username':'tim',
            'password':'wowmonkey1234',
        }
    def test_sign_out_homepage(self):
        user = User.objects.create_user(username='tim', password='Monkey1234')
        self.client.login(username='tim', password='Monkey1234')
        answer = self.client.post(self.url,self.data)
        self.assertEqual(answer.status_code,302)
        self.assertTrue(User.objects.filter(username='tim').exists())
