from . import views
from django.urls import path
 
urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('tasks', views.taskpush, name='task-create'),
    

]