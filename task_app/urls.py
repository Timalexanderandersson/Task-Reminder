from . import views
from django.urls import path
 
urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('tasks/', views.taskpush, name='task-create'),
    path('delete/<int:pk>/', views.DeleteTask.as_view(), name='delete_site'),
    path('update/<int:pk>/', views.UpdateTask.as_view(), name='updating_task'),
]