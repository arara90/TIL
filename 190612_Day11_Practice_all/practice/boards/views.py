from django.shortcuts import render,redirect
from .models import Board, Comment

# Create your views here.
def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)

def new(request):
    if request.method == 'POST':
        print('POST')
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        board = Board(title=title, content=content, image=image)
        board.save()
        # redirect는 url을 찾아간다! 어디url? project url먼저!
        return redirect(f'/boards/{board.pk}')
    else:
        print('h')
        # render는 BASE_DIR -> 구담에 app의 templates 을 찾는다!
        return render(request, 'boards/new.html')

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    comments = board.comment_set.all()
    context = {'board':board, 'comments': comments}
    return render(request,'boards/detail.html', context)


def edit(request, pk):
    board = Board.objects.get(pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        print(image)

        board.title = title
        board.content = content
        board.image = image

        board.save()

        return redirect(f'/boards/{pk}')

    else:
        context = {'board': board}
        return render(request, 'boards/edit.html', context)


def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('/boards/')
    else:
        return redirect(f'/boards/{board.pk}')

def new_comment(request, pk):
    content = request.POST.get('content')
    comment = Comment(content=content, board_id=pk)
    comment.save()
    return redirect(f'/boards/{pk}')

def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    board_pk = comment.board_id
    comment.delete()
    return redirect(f'/boards/{board_pk}')