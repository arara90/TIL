from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import UserCustomChangeForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index') #app:path 그래서 urls에 app_name을 설정한 것이야.
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method == 'POST':
        # request : 요청정보 / request.POST : 유저정보
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            print(form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context={'form' : form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        auth_logout(request)
        print('logout')
        return redirect('boards:index')

    else:
        print('logout:get')
        return redirect('boards:index')

def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('boards:index')
    else :
        return redirect('boards:index')

def edit(request):
    if request.method == 'POST':
        # instance : 수정 로직에서 작성한 글을 가져올 때,
        # 즉, 새로운 정보는 request.POST (to) / instance = request.user는 기존의 정보 (from)
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
        context = {'form': form }
        # print('?')
        return render(request, 'accounts/edit.html', context)


