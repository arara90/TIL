from django.shortcuts import render,redirect
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}

    return render(request, 'board/index.html', context)

def new(request):
    return render(request, 'board/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title, content=content)
    board.save()

    return redirect(f'/board/{board.pk}/')

def detail(request,pk):
    board = Board.objects.get(pk=pk)
    context = {'board': board}
    return render(request, 'board/detail.html', context)


def edit(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, 'board/edit.html', context)

def update(request,pk):

    board = Board.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')

    board.title = title
    board.content = content
    board.save()

    return redirect(f'/board/{board.pk}/')

def delete(request,pk):

    board = Board.objects.get(pk=pk)
    board.delete()

    return redirect('/board/')