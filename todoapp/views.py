from django.shortcuts import render, redirect
from .forms import TodoForm, CreateForm
from .models import Todo
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user
    todos = Todo.objects.filter(author=user).order_by('-id')
    obj = request.GET.get('a')
    if obj:
        todos = todos.filter(status__exact=obj)
    search = request.GET.get('i')
    if search:
        todos = todos.filter(title__icontains=search)
    ctx = {
        'todos': todos
    }
    return render(request, 'index.html', ctx)


@login_required
def single(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'single.html', ctx)


@login_required
def create(request):
    form = CreateForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.status = 0
        obj.save()
        return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'create.html', ctx)


@login_required
def delete(request, pk):
    obj = Todo.objects.get(id=pk)
    # yes = request.POST.get('yes')
    # no = request.POST.get('no')
    # if yes:
    obj.delete()
    #     return redirect('/')
    # elif no:
    #     return redirect('/')
    return redirect('/')
