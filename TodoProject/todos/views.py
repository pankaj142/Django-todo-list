from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.

def list_todo_items(request):
    context = {'todo_list' : Todo.objects.all()}
    # return HttpResponse('list of todos')
    return render(request, 'todos/todo_list.html', context)

def insert_todo_item(request):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list')

def remove_todo_item(request, todo_id):
    delete_todo = Todo.objects.get(id=todo_id)
    delete_todo.delete()
    return redirect('/todos/list')