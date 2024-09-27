from . import views
from django.urls import path
 
urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('tasks/', views.taskpush, name='task-create'),
    path('register/', views.signing_up, name="register"),
    path('login/', views.AccountLogin, name="login"),
    path('logout/', views.AccountLogout, name="logout"),
    path('delete/<int:pk>/', views.DeleteTask.as_view(), name='delete_site'),
    path('update/<int:pk>/', views.UpdateTask.as_view(), name='updating_task'),
]