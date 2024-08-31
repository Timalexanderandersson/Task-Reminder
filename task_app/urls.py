from . import views
from django.urls import path
 
urlpatterns = [
    path('', views.TaskListAll.as_view(), name='Home'),
]