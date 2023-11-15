from django.shortcuts import render, redirect, get_object_or_404
from base.models import Todo
from .forms import *

def ListAllTodos(request):
    todo = Todo.objects.all()
    return render(request,"ui/list_all.html",{'todos':todo})

def CreateTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_all_todos')
    else:
        form = TodoForm()
    return render(request, "ui/create.html", {'form': form})

def DeleteTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('list_all_todos')

def EditTodo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list_all_todos')
    else:
        form = TodoForm(instance=todo)

    return render(request, "ui/edit_todo.html", {'form': form, 'todo': todo})