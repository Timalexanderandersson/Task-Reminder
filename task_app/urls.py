from . import views
from django.urls import path
 
urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('tasks', views.taskpush, name='task-create'),
    path('newpage/<int:task_id>/', views.newpage, name='newpage'),
    path('delete-task/<int:task_id>/', views.delete_task_list, name='delete_page'),
    

]