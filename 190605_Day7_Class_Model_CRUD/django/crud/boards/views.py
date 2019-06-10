from django.shortcuts import render, redirect
from .models import Board


# Create your views here.

def index(request):

    boards = Board.objects.order_by('-id').all()

    # articles = []
    # for item in boards:
    #     articles.append({'title': item.title, 'content': item.content})

    context = {'articles':  boards}

    return render(request, 'boards/index.html', context)

def new(request):
    return render(request, 'boards/new.html')

def create(request):

    title = request.POST.get('title')
    #request.GET는 dict라 .get()을 사용하는 것임
    content = request.POST.get('content')
    # #sol2
    board = Board(title=title, content=content)
    board.save()

    return redirect(f'/boards/{board.pk}/')

def detail(request, pk):

    board = Board.objects.get(pk=pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)

def delete(request, pk):

    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board': board }
    return render(request, 'boards/edit.html', context)

def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect(f'/boards/{board.pk}')