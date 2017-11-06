from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def index(request):
    
    todos = Todo.objects.filter(owner=request.user)[:10]
    context = {
        'todos':todos
    }
    return render(request, 'todos/index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
            'todo':todo
    }
    return render(request, 'todos/details.html', context)

def add(request):
    if request.user.is_authenticated():
        if(request.method == 'POST'):
            title = request.POST['title']
            text = request.POST['text']
            owner = request.user
    
            todo = Todo(title=title, text=text, owner=owner)
            todo.save()
    
            return redirect('/todos')
        else:
            return render(request, 'todos/add.html')
    else:
        return redirect('/')

def delete(request, id):
    if request.user.is_authenticated():
        todo = Todo.objects.get(id=id)
        if todo.owner == request.user:
            todo.delete()
        return redirect('/todos')
    else:
        return redirect('/')
