# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
#bring in the HttpResponse
from django.http import HttpResponse
#bring in the models
from .models import Todo

# Create your views here.

# when index is loaded give us the request object
def index(request):
    todos = Todo.objects.all()[:10]
   
    lexicon = {
        'todos': todos
    }
    
    return render(request, 'index.html', lexicon)

def details(request, id):
    todo = Todo.objects.get(id=id)
   
    lexicon = {
        'todo': todo
    }
    return render(request, 'details.html', lexicon)

def add(request):
    if (request.method == "POST"):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')
    
