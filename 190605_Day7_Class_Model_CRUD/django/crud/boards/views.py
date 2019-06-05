from django.shortcuts import render
from .models import Board

# Create your views here.

def index(request):

    boards = list(Board.objects.all())
    print(type(boards[0]))

    articles = []
    for item in Board.objects.all():
        articles.append({'title': item.title, 'content': item.content})

    context = { 'articles' : articles}

    return render(request, 'boards/index.html',context)

def new(request):
    return render(request, 'boards/new.html')

def create(request):

    title = request.POST.get('title')
    #request.GET는 dict라 .get()을 사용하는 것임
    content = request.POST.get('content')

    #sol1
    #board = Board()
    #board.title = title
    #board.content = content
    #board.save()

    # #sol2
    board = Board(title=title, content=content)
    board.save()


    return render(request, 'boards/create.html')

