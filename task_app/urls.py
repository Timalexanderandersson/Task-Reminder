from . import views
from django.urls import path
 
urlpatterns = [
    path('', views.taskpush, name='Homepage'),
]