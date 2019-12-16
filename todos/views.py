from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todos

# Create your views here.


def list_todo_items(request):
    context = {'todo_list': Todos.objects.all()}
    return render(request, 'todos/todo_list.html', context)


def insert_todo_item(request: HttpRequest):
    todo = Todos(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todos.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')


def deleteAll(request):
    Todos.objects.all().delete()
    return redirect('/todos/list/')
