from . import views
from django.urls import path
 
urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('task/search/', views.search_here, name='search_here'),
    path('tasks/', views.taskpush, name='task-create'),
    path('register/', views.signing_up, name="register"),
    path('login/', views.accountlogin, name="login"),
    path('logout/', views.accountlogout, name="logout"),
    path('delete/<int:pk>/', views.DeleteTask.as_view(), name='delete_site'),
    path('update/<int:pk>/', views.UpdateTask.as_view(), name='updating_task'),
    path('contact/',views.contact_form, name="contact"),
    path('success/',views.form_success, name="form_success"),

]