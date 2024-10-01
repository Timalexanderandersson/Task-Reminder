from django.test import TestCase
from .forms import PostUser, SigningUp, SignIn

# Create your tests here.
class PostUserTest(TestCase):

    def test_if_form_valid(self):
        form_post = PostUser({
            'title':'car wash',
            'description':'wash my car',
            'completed':False,
            'due_date':'2024-05-06',
            'time_date':'12:30',
        })
        
        self.assertTrue(form_post.is_valid(), msg="Form is invalid")

    def test_if_form_without_title(self):
        form_post = PostUser({
            'title':'',
            'description':'wash my car',
            'completed':False,
            'due_date':'2024-05-06',
            'time_date':'12:30',
        })
        
        self.assertFalse(form_post.is_valid(), msg="Form is invalid without the title")

    def test_if_form_without_description(self):
        form_post = PostUser({
            'title':'car wash',
            'description':'',
            'completed':False,
            'due_date':'2024-05-06',
            'time_date':'12:30',
        })
        
        self.assertFalse(form_post.is_valid(), msg="Form is invalid without the description")

    def test_if_form_without_completed(self):
        form_post = PostUser({
            'title':'car wash',
            'description':'',
            'completed':None,
            'due_date':'2024-05-06',
            'time_date':'12:30',
        })
        
        self.assertFalse(form_post.is_valid(), msg="Form is invalid without the completed")    

    def test_if_form_without_due_date(self):
        form_post = PostUser({
            'title':'car wash',
            'description':'',
            'completed':None,
            'due_date':'',
            'time_date':'12:30',
        })
        
        self.assertFalse(form_post.is_valid(), msg="Form is invalid without the due_date") 

    def test_if_form_without_time_date(self):
        form_post = PostUser({
            'title':'car wash',
            'description':'',
            'completed':None,
            'due_date':'',
            'time_date':'',
        })
        
        self.assertFalse(form_post.is_valid(), msg="Form is invalid without the time_date")

class SignInTest(TestCase):
    '''
    test for all sign in.
    '''
    def test_sign_in_is_valid(self):
        form_sign = SignIn({
        'username':'Tim',
        'password':'monkey461'
        })
    
        self.assertTrue(form_sign.is_valid(), msg="Form should be valid.")

    def test_sign_in_without_username(self):
        form_sign = SignIn({
        'username':'',
        'password':'monkey461'
        })
    
        self.assertFalse(form_sign.is_valid(), msg="Form should be invalid without username.")

    def test_sign_in_without_password(self):
        form_sign = SignIn({
        'username':'Tim',
        'password':''
        })
    
        self.assertFalse(form_sign.is_valid(), msg="Form should be invalid without password.")

class SignUpTest(TestCase):
    '''
    test for sign up form.
    '''
    def test_sign_up_is_valid(self):
        form_register = SigningUp({
        'username': 'Tim',
        'email': 'timandersson@example.com', 
        'password1': 'wowthispassword123',
        'password2': 'wowthispassword123'
    })
        self.assertTrue(form_register.is_valid(), msg="Form should be valid.")

    def test_sign_up_without_username(self):
        form_register = SigningUp({
        'username': '',
        'email': 'timandersson@example.com', 
        'password1': 'wowthispassword123',
        'password2': 'wowthispassword123'
    })
        self.assertFalse(form_register.is_valid(), msg="Form should have invalid username.")

    def test_sign_up_without_email(self):
        form_register = SigningUp({
        'username': 'Tim',
        'email': '', 
        'password1': 'wowthispassword123',
        'password2': 'wowthispassword123'
    })
        self.assertFalse(form_register.is_valid(), msg="Form should have invalid email.")

    def test_sign_up_without_first_password(self):
        form_register = SigningUp({
        'username': 'Tim',
        'email': 'timandersson@example.com', 
        'password1': '',
        'password2': 'wowthispassword123'
    })
        self.assertFalse(form_register.is_valid(), msg="Form should have invalid first_password.")

    def test_sign_up_without_second_password(self):
        form_register = SigningUp({
        'username': 'Tim',
        'email': 'timandersson@example.com', 
        'password1': 'wowthispassword123',
        'password2': ''
    })
        self.assertFalse(form_register.is_valid(), msg="Form should have invalid second_password.")    