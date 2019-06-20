from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
from IPython import embed
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def index(request):
    boards = Board.objects.order_by('-id')
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)


def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        # embed()
        # 유효성 검사 : is_valid(): True / False 형태로 결과를 나타냄
        # 빈값인지, 자료형이 맞는지
        if form.is_valid():
            # # cleaned_data: dict형으로 만들어준다.
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # board = Board.objects.create(title=title, content=content)
            board= form.save()

            return redirect('boards:detail', board.pk)

    else:
        form = BoardForm()

     # get이거나 post이지만 유효성검사 통과 못하면
    context = {'form':form}
    return render(request, 'boards/form.html', context)


def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board':board}
    return render(request, 'boards/detail.html', context)


def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')

    context = {'board':board}
    return render(request, 'boards/detail.html', context)
    # else:
    #     context = {'board':board}
    #     return render(request, 'boards/detail.html', context)


def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            # board.title = form.cleaned_data.get('title')
            # board.content = form.cleaned_data.get('content')
            # board.save()

            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                form.save()
                return redirect('boards:detail', board.pk)
    else:
        # form = BoardForm(initial=board.__dict__)
        form = BoardForm(instance=board)
    print(form)
    context = {'form': form, 'board': board}
    return render(request, 'boards/form.html', context)

def photo(request):
    return render(request, 'boards/photo.html')

@login_required
@require_POST
def comments_delete(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return redirect('boards:detail', board_pk)
    else:
        comment.delete()
        return redirect('boards:detail', board_pk)

@login_required
def like(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    # user = request.user

    # 이미 좋아요. 눌렀던 사람이 또 누르면 취소.
    # if board.like_users.filter(pk=user.pk).exist():
    if request.user in board.like_users.all():
        board.like_users.remove(request.user) #관계 삭제

    # 좋아요 등록
    else:
        board.like_users.add(request.user)

    return redirect('boards:index')
