from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListAllTodos, name='list_all_todos'),
    path('create/', views.CreateTodo, name='create_todo'),
    path('delete/<int:todo_id>/', views.DeleteTodo, name='delete_todo'),
    path('edit/<int:todo_id>/', views.EditTodo, name='edit_todo'),
]
