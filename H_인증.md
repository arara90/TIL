[TOC]

### 인증

-----



#### 1. 기본설정

1. $ python manage.py startapp accounts(django > myform)

2. setting.py

   ```python
   INSTALLED_APPS = [
       'accounts',
       'boards',
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'django_extensions',
       'bootstrap4',
   ]
   ```

3. myform\url.py

   ```python
   urlpatterns = [
       path('accounts', includ('accounts.urls')),
       path('boards/', include('boards.urls')),
       path('admin/', admin.site.urls),
   ]
   ```

4. accounts\urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'accounts'
   
   urlpatterns = [
   
   ]
   ```

5. $ mkdir -p templates/accounts(django > myform > accounts)

-----



#### 2. 회원가입 기능

1. views.py

   ```python
   from django.shortcuts import render, redirect
   from django.contrib.auth.forms import UserCreationForm
   
   def signup(request):
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('accounts:index')
       else:
           form = UserCreationForm()
       context = {'form':form}
       return render(request, 'accounts/signup.html', context)
   ```

2. urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'accounts'
   
   urlpatterns = [
       path('signup/', views.signup, name='signup'),
   ]
   ```

3. signup.html

   ```html
   {% extends 'boards/base.html' %}
   {% load bootstrap4 %}
   
   {% block body %}
   <h1 class="text-center">회원 가입</h1>
   <hr>
   <form action="" method="POST">
       {% csrf_token %}
       {% bootstrap_form form %}
   
       {% buttons %}
           <button type="submit" class="btn btn_primary">회원가입</button>
       {% endbuttons %}
   </form>
   {% endblock %}
   ```

-----



#### 3. 로그인 기능

1. 기본 개념

   1. 쿠키와 세션

      세션아이디를 쿠키에 넣어 보낸다.

      쿠키는 보안에 큰 문제 없는 정보를 담고 있고, 세션은 보안에 중요한 정보를 담고 있다.

   2. 로그인한다 == 세션을 만든다

2. view.py

   ```python
   from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
   from django.contrib.auth import login as auth_login
   
   def login(request):
       if request.method =='POST':
           form = AuthenticationForm(request, request.POST) # request: 요청정보, form.get_user():user정보
           if form.is_valid():
               auth_login(request, form.get_user()) 
               return redirect('boards:index')
       else:
           form = AuthenticationForm()
       context = {'form':form}
       return render(request, 'accounts/login.html', context)
   ```

3. urls.py

   ```python
   path('login/', views.login, name='login')
   ```

4. login.html

   ```html
   {% extends 'boards/base.html' %}
   {% load bootstrap4 %}
   
   {% block body %}
   <h1 class="text-center">로그인</h1>
   <hr>
   <form action="" method="POST">
       {% csrf_token %}
       {% bootstrap_form form %}
   
       {% buttons %}
           <button type="submit" class="btn btn_primary">로그인</button>
       {% endbuttons %}
   </form>
   {% endblock %}
   ```

5. base.html(django > myform > boards > templates > boards > base.html)

   ```html
   <body>
       <div class="container">
           <h1>안녕, {{ user.username }}</h1>
           {% block body %}
           {% endblock %}
       </div>
   </body>
   ```

-----



#### 4. 로그아웃 기능

1. views.py

   ```python
   from django.contrib.auth import logout as auth_logout
   
   def logout(request):
       if request.method == 'POST':
           auth_logout(request)
           return redirect('boards:index')
       else:
           return redirect('boards:index')
   ```

2. urls.py

   ```python
   path('logout/', views.logout, name='logout')
   ```

-----



#### 5. 회원탈퇴 기능

1. views.py

   ```python
   def delete(request):
       if request.method == 'POST':
           request.user.delete()
           return redirect('boards:index')
       else:
           return redirect('boards:index')
   ```

2. urls.py

   ```python
   path('delete/', views.delete, name='delete'),
   ```

3. base.html (로그인되어있을때, boards에서 회원탈퇴 버튼 뜨도록)

   ```html
   {% if user.is_authenticated %}
       <h1>안녕, {{ user.username }}</h1>
       <hr>
       <form action="{% url 'accounts:logout' %}" method="POST">
           {% csrf_token %}
           <input type="submit" value="로그아웃">
       </form>
       <form action="{% url 'accounts:delete' %}" method="POST">
           {% csrf_token %}
           <input type="submit" value="회원탈퇴">
       </form>
   ```

-----



#### 6. 링크 연결

1. base.html(로그인 상태--> 로그아웃, 로그아웃 상태 --> 로그인, 회원가입 뜨도록)

   ```html
   <body>
       <div class="container">
           {% if user.is_authenticated %}
               <h1>안녕, {{ user.username }}</h1>
               <hr>
               <form action="{% url 'accounts:logout' %}" method="POST">
                   {% csrf_token %}
                   <input type="submit" value="로그아웃">
               </form>
           {% else %}
               <a href="{% url 'accounts:login' %}">로그인</a><br>
               <a href="{% url 'accounts:signup' %}">회원가입</a>
           {% endif %}
           
           {% block body %}
           {% endblock %}
   ```

2. index.html(로그인 상태--> 글작성, 로그아웃 상태 --> 로그인 페이지로)

   ```html
   {% if user.is_authenticated %}
           <a href="{% url 'boards:create' %}">[글 작성]</a>
       {% else %}
           <a href="{% url 'accounts:login' %}">[글을 작성하려면 로그인 해주세요]</a>
       {% endif %}
   ```

3. views.py (회원가입시, 로그인 유지되도록 하기)

   user = form.save()
   auth_login(request, user)

   ```python
   def signup(request):
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               #form.save()
               user = form.save()
               auth_login(request, user)
               return redirect('boards:index')
   ```

4. views.py (로그인된 상태에서 회원가입 페이지 뜨지 않도록)

   ```python
   def signup(request):
       if request.user.is_authenticated:
           return redirect('boards:index')
       if request.method == 'POST':
   ```

5. views.py (로그인된 상태에서 로그인 페이지 뜨지 않도록)

   ```python
   def login(request):
       if request.user.is_authenticated:
           return redirect('boards:index')
       if request.method =='POST':
   ```

-----



#### 7. 회원정보 수정 기능

1. views.py

   ```python
   from django.contrib.auth.forms import UserChangeForm
   
   def edit(request):
       if request.method == 'POST':
           form = UserChangeForm(request.POST, instance=request.user)
           if form.is_valid():
               form.save()
               return redirect('boards:index')
       else:
           form = UserChangeForm(instance=request.user)
       context = {'form':form}
       return render(request, 'accounts/edit.html', context)
   ```

2. urls.py

   ```python
   path('edit/', views.edit, name='edit')
   ```

3. edit.html

   ```html
   {% extends 'boards/base.html' %}
   {% load bootstrap4 %}
   
   {% block body %}
   <h1 class="text-center">회원정보 수정</h1>
   <hr>
   <form action="" method="POST">
       {% csrf_token %}
       {% bootstrap_form form %}
   
       {% buttons %}
           <button type="submit" class="btn btn_primary">회원정보 수정</button>
       {% endbuttons %}
   </form>
   {% endblock %}
   ```

4. base.html

   ```html
   {% if user.is_authenticated %}
       <h1>안녕, {{ user.username }}</h1>
       <hr>
       <a href="{% url 'accounts:edit' %}">회원정보 수정</a>
   ```

5. 회원정보 수정 페이지에서 필요한 정보만 띄워주기

   forms.py(django > myforms > accounts > forms.py)

   ```python
   from django.contrib.auth.forms import UserChangeForm
   from django.contrib.auth import get_user_model
   
   class UserCustomChangeForm(UserChangeForm):
       class Meta:
           model = get_user_model()
           fields = ('email', 'first_name', 'last_name') # 수정할 수 있도록 지정 할 field
   ```

6. views.py

   ```python
   from  .forms import UserCustomChangeForm
   
   # UserChangeForm --> UserCustomChangeForm
   
   def edit(request):
       if request.method == 'POST':
           #form = UserChangeForm(request.POST, instance=request.user)
           form = UserCustomChangeForm(request.POST, instance=request.user)
           if form.is_valid():
               form.save()
               return redirect('boards:index')
       else:
           #form = UserChangeForm(instance=request.user)
           form = UserCustomChangeForm(instance=request.user)
       context = {'form':form}
       return render(request, 'accounts/edit.html', context)
   ```

-----



#### 8. 비밀번호 변경 기능

1. views.py

   ```python
   from django.contrib.auth.forms import PasswordChangeForm
   
   def change_password(request):
       if request.method == 'POST':
           form = PasswordChangeForm(request.user, request.POST ) # request.user: 요청자의 정보, request.POST: 기존 비밀번호, 변경된 비밀번호, 
           if form.is_valid():
               form.save()
               return redirect('boards:index')
       else:
           form = PasswordChangeForm(request.user)
       context = {'form':form}        
       return render(request, 'accounts/change_password.html', context)
   ```

2. urls.py

   ```python
   path('password/', views.change_password, name='change_password')
   ```

3. change_password.html

   ```html
   {% extends 'boards/base.html' %}
   {% load bootstrap4 %}
   
   {% block body %}
   <h1 class="text-center">비밀번호 변경</h1>
   <hr>
   <form action="" method="POST">
       {% csrf_token %}
       {% bootstrap_form form %}
   
       {% buttons %}
           <button type="submit" class="btn btn_primary">비밀번호 변경</button>
       {% endbuttons %}
   </form>
   {% endblock %}
   ```

4. base.html

   ```html
   <a href="{% url 'accounts:edit' %}">회원정보 수정</a><br>
   <a href="{% url 'accounts:change_password' %}">비밀번호 변경</a><br>
   ```

5. views.py (비밀번호 변경시에도 로그인 상태 유지되도록)

   user = form.save()
   update_session_auth_hash(request, user)

   ```python
   from django.contrib.auth import update_session_auth_hash
   
   def change_password(request):
       if request.method == 'POST':
           form = PasswordChangeForm(request.user, request.POST ) # request.user: 요청자의 정보, request.POST: 기존 비밀번호, 변경된 비밀번호,
           if form.is_valid():
               #form.save()
               user = form.save()
               update_session_auth_hash(request, user)
               return redirect('boards:index')
   ```