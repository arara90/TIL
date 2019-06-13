from django.shortcuts import render,redirect
from .models import Board,Comment

# Create your views here.
def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}

    return render(request, 'board/index.html', context)

def new(request):
    print(request.method)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:detail', board.pk)

    else:
        return render(request, 'board/new.html')

def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    context = {'board': board, 'comments': comments}
    return render(request, 'board/detail.html', context)


def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        board.title = title
        board.content = content
        board.save()

        return redirect('board:detail', board.pk)

    else:
        context = {'board': board}
        return render(request, 'board/edit.html', context)

# POST 방식으로 수정하기
def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    board.delete()
    return redirect('board:index')

def comments_create(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method=='POST':
        comment = Comment()
        # coment.board = board #알아서 id 뽑아주지만 아래처럼 명시적으로 써주자.
        comment.board_id = board.pk
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('board:detail', board.pk)
    else:
        return redirect('board:detail', board.pk)

def comments_edit(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'POST':
        print(request.POST.get('content'))
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('board:detail', board_pk)

    else:
        print('hio')
        context = {'comment': comment}
        return render(request,'board/comment_edit.html', context)


def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('board:detail', board_pk)

    else:
        comment.delete()
        return redirect('board:detail', board_pk)


