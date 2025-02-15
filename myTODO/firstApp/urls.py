from django.urls import path

from . import views
from . views import *

urlpatterns = [
    path('', main_page),
    path('user_signup/', user_signup, name = 'user_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('main_page/', main_page, name='main_page'),
    path('delete/<int:d_id>/', views.delete, name='delete'),
    path('logout/', views.user_logout, name='user_logout'),
    path('todo_update/<int:u_id>', views.todo_update, name= 'todo_update')
]