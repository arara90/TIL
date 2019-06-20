[TOC]

### 권한

-----



#### 1. 글 작성, 수정 권한 설정

​	로그아웃상태에서 주소창에 /boards/create입력하면 글 작성 페이지로 이동함

1. boards/views.py

   ```python
   from django.contrib.auth.decorators import login_required
   
   @login_required
   def create(request):
       
   @login_required
   def update(request, board_pk):
   ```

2. 로그아웃 상태에서 주소창으로 글작성 페이지로 이동 후, 로그인하면 글작성 페이지로 넘어가도록

   accounts/views.py

   return redirect(request.GET.get('next'), 'boards:index')

   ```python
   def login(request):
       if request.user.is_authenticated:
           return redirect('boards:index')
       if request.method =='POST':
           form = AuthenticationForm(request, request.POST) # request: 요청정보, form.get_user():user정보
           if form.is_valid():
               auth_login(request, form.get_user())
               return redirect(request.GET.get('next'), 'boards:index')
   ```


-----



#### 2. user-board 무결성

1. user 회원탈퇴 시, 해당 user가 작성한 글 삭제되도록

   1. boards\models.py

      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 추가

      ```python
      from django.conf import settings
      
      class Board(models.Model):
          user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      ```

   2. $ python manage.py makemigrations

   3. $ python manage.py migrate

2. boards\views.py

   ```python
   def create(request):
       if request.method == 'POST':
          form = BoardForm(request.POST) # 사용자가 create.html에서 날린 데이터를
          #embed()
          if form.is_valid(): # form이 유효하면(is_vaild: 유효성 검사--> boolean값 리턴)
              board = form.save(commit=False) #commit=False: 저장 보류
              board.user = request.user #request.user: 로그인된 user 정보/ board.user: board class의 user field
              board.save()
              return redirect('boards:detail', board.pk)
   ```

3. index.html

   ```html
   <h1 class="text-center">INDEX</h1>
   <hr>
       {% for board in boards %}
           <p><b>글 작성자: {{ board.user }}</b></p>
           <p>글 번호: {{ board.pk }}</p>
           <p>글 제목: {{ board.title }}</p>
           <a href="{% url 'boards:detail' board.pk %}">[글 상세보기]</a><br>
           <hr>
       {% endfor %}
   ```

-----



#### 3. 글 수정/삭제 권한

1. 글 작성자가 로그인 되었을 때에만 detail페이지에서 수정,삭제 버튼 보이도록

   detail.html

   ```html
   {% if user == board.user %}
   	<a href="{% url 'boards:update' board.pk %}">[수정]</a><br>
   	<form action="{% url 'boards:delete' board.pk %}" method="POST">
       {% csrf_token %}
       <input type="submit" value="[삭제]">
   {% endif %}
   ```

2. 글 작성자에게만 글 삭제, 수정 권한 부여

   boards\views.py

   ```python
   @login_required
   def update(request, board_pk):
       board = get_object_or_404(Board, pk=board_pk)
       if board.user == request.user:
           if request.method == 'POST':
               form = BoardForm(request.POST, instance=board)
               if form.is_valid():
                   form.save()
                   return redirect('boards:detail', board_pk)
           else:
               form = BoardForm(instance=board)
       else:
           return redirect('boards:index')
       context = {'form':form, 'board':board}
       return render(request, 'boards/form.html', context)
   
   def delete(request, board_pk):
       board = get_object_or_404(Board, pk=board_pk)
       if board.user == request.user:
           if request.method =='POST':
               board.delete()
               return redirect('boards:index')
           else:
               return redirect('boards:detail', board_pk)
       else:
           return redirect('boards/index')
   ```

-----



### 댓글

#### 1.댓글 작성

1. boards\models.py

   ```python
   class Comment(models.Model):
       content = models.CharField(max_length=100)
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       board = models.ForeignKey(Board, on_delete=models.CASCADE)
       class Meta:
           ordering = ('-pk',) # 최신 댓글이 위에 오도록
   ```

2. boards/forms.py

   ```python
   from .models import Comment
   
   class CommentForm(forms.ModelForm):
       class Meta:
           model = Comment
           fields = ['content',]
   ```

3. boards\admin.py

   ```python
   from .models import Comment
   
   class CommentAdmin(admin.ModelAdmin):
       list_display = ('content',)
   
   admin.site.reguster(Comment, CommentAdmin)
   ```

4. boards\views.py

   ```python
   from .forms import CommentForm
   
   def detail(request, board_pk):
       #board = Board.objects.get(pk=board_pk)
       board = get_object_or_404(Board, pk=board_pk) # Board에 해당하는 pk있으면 가져오고, 없으면 404 error 띄운다
       comments = board.comment_set.all()
       comment_form = CommentForm()
       context = {'board': board, 'comments':comments, 'comment_form':comment_form,}
       return render(request, 'boards/detail.html', context)
   
   
   
   from django.views.decorators.http import require_POST
   
   @login_required
   @required_POST # POST요청 외의 요청이 들어오면 405 error 띄운다.
   def comments_create(request, board_pk):
       comment_form = CommentForm(request.POST)
       if comment_form.is_valid():
           comment = comment_form.save(commit=False) # user 정보 필요하므로 잠시 hold
           comment.user = request.user # comment.user에 요청자의 정보를 넣는다
           comment.board_id = board_pk
           comment.save()
           return redirect('boards:detail', board_pk)
   ```

5. boards\urls.py

   ```python
   path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
   ```

6. boards\detail.html

   ```html
   <hr>
   <h3>댓글</h3>
   {% for comment in comments|dictsortreversed:'pk' %} <!-- |dictsortreversed:'pk': 최신 댓글이 위에 위치 하도록 -->
   	<p><b>{{ comment.user }}님의 댓글: {{ comment.content }}</b></p>
   {% empty %}
   	<p><b>댓글이 없습니다.</b></p>
   {% endfor %}
   <hr>
   
   <h3>댓글 작성</h3>
   <form action="{% url 'boards:comments_create' board.pk %}" method="POST">
       {% csrf_token %}
       {{ comment_form.as_p }}
       <input type="submit" value="댓글 작성">
   </form>
   <a href="{% url 'boards:index' %}">[메인페이지]</a><br>
   ```

----



#### 2. 댓글 권한

1. 로그인되었을 때에만 detail 페이지에서 댓글작성 폼이 나타나도록

   1. boards\detail.html

      ```html
      <h3>댓글 작성</h3>
          {% if user.is_authenticated %}
              <form action="{% url 'boards:comments_create' board.pk %}" method="POST">
                  {% csrf_token %}
                  {{ comment_form.as_p }}
                  <input type="submit" value="댓글 작성">
              </form>
          {% else %}
              <a href="{% url 'accounts:login' %}">댓글 작성을 위해 로그인이 필요합니다</a><br>
          {% endif %}
      ```

----



#### 3. 댓글 삭제

​	댓글 작성자에게만 댓글삭제 버튼이 보이도록

1. boards\views.py

   ```python
   from .models import Comment
   
   @login_required
   @require_POST
   def comments_delete(request, board_pk, comment_pk):
       comment = get_object_or_404(Comment, pk=comment_pk)
       if request.user != comment.user:
           return redirect('boards:detail', board_pk)
       else:
           comment.delete()
           return redirect('boards:detail', board_pk)
   ```

2. boards\urls.py

   ```python
   path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete')
   ```

3. boards\detail.html

   ```html
    <h3>댓글</h3>
       {% for comment in comments|dictsortreversed:'pk' %} <!-- |dictsortreversed:'pk': 최신 댓글이 위에 위치 하도록 -->
           <p><b>{{ comment.user }}님의 댓글: {{ comment.content }}</b></p>
           {% if user == comment.user %}
               <form action="{% url 'boards:comments_delete' board.pk comment.pk %}" method="POST">
                   {% csrf_token %}
                   <input type="submit" value="[댓글삭제]">
               </form>
           {% endif %}
       {% empty %}
           <p><b>댓글이 없습니다.</b></p>
       {% endfor %}
   ```