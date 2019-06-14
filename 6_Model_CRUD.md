1.  새 **프로젝트** 시작

   * django 폴더에서 **django-admin startproject crud**

2.  **APP** 생성

   * crud로 이동해서 **python manage.py startapp boards**

     ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\structure.PNG)

   * django 폴더내에 crud 프로젝트와 intro 프로젝트(기존에 있던것, 해당문서에서 만들지 않았음)가 있는 상태

   * crud 프로젝트내에 crud는 기본 생성된것이고, 위에서 생성한 boards 앱이 만들어진 것을 볼 수 있다.  

3. APP 출생 신고

   * setting.py 

     * INSTALLED_APPS에 등록

     * ```python
       LANGUAGE_CODE = 'ko-kr'
       TIME_ZONE = 'Asia/Seoul'
       ```
  
     * base.html (프로젝트내 모든 APP에 적용할 templates BASE_DIR 설정) : 
     
       >  'DIRS': [os.path.join(BASE_DIR, 'Project명', 'templates')]
     
       ```python
       TEMPLATES = [
           {
               'BACKEND': 'django.template.backends.django.DjangoTemplates',
               'DIRS': [os.path.join(BASE_DIR, 'ARA', 'templates')],
               'APP_DIRS': True,
               'OPTIONS': {
                   'context_processors': [
                       'django.template.context_processors.debug',
                       'django.template.context_processors.request',
                       'django.contrib.auth.context_processors.auth',
                       'django.contrib.messages.context_processors.messages',
                   ],
               },
           },
       ]
       
       ```
     
       ![base.html의 위치](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\base.PNG)
     
       기본 project 폴더내에 templates 디렉토리를 만들고 그 안에 base.html
     

### 1. Model 정의

```python
#models.py

from django.db import models

# Create your models here.
class Board(models.Model): #model.Model을 상속받는다.
    #CharField : max_length가 필수
    title = models.CharField(max_length=10)
    content = models.TextField()
    #auto_now_add=True: '최초 insert'시 언제 작성되었는지
    created_at = models.DateTimeField(auto_now_add=True)
```

## 2. 설계도

1. 명령어 : python manage.py **makemigrations**

* 설계도를 만드는 것 

Migrations for 'boards':
  boards\migrations\0001_initial.py

   - **Create model Board**

     ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\migrations.PNG)

```python
#migration > 0001_initial.py확인

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

```

2. **settings.py 에서 use Time Zone 수정**

```python
USE_I18N = True
USE_L10N = True
#변경 True -> False
USE_TZ = False
```

데이터 저장시 생성된 시간이 위에서 설정한 실제 서울 시간으로 반영된다.

3. **Board Class에 method 추가**

```python
updated_at = models.DateTimeField(auto_now=True)	
```

method 수정 후에는 반드시 다시 명령어 실행  **python manage.py makemigrations**

```
# 결과
Migrations for 'boards':
  boards\migrations\0002_board_updated_at.py
    - Add field updated_at to board

```

![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\migrations2.PNG)



## 3. **실제 테이블 생성**(설계도 반영)

* 명령어 : python manage.py **migrate**



## 4. CRUD

### 4-1) 'C'rud ( **Create** )

**명령어 : python manage.py shell**

![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\shell.PNG)

1. **object 매니저**

   ```
   from boards.models import Board
   Board.objects.all()
   ```

   : objects는 object를 관리하는 매니저 / DB와 통신하게 해줌 (통역사) 

![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\shell2.PNG)

2. **객체 생성**

   board = Board()

   

3. **Insert**

   board.title = 'first'
   board.content = 'django'

4. **save ( = commit)**

   * 4번을 실행하고 실제 board를 살펴보면 (명령어 : board) 

     <Board: Board object (None)>   

     즉, 실제 반영이 되지 않았다는 것

   

   * 실제 반영을 하려면 반드시 save를 해야한다. (db에서의 commit과 비슷)

     **board.save()**

     다시 board를 입력해보면 <Board: Board object (1)> 로 실제 반영된 것을 알 수 있다.

     ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\save.PNG)

     



* 객체 생성법

  1) board = Board() -> board.save()

  2) board = Board(title='second',content ='django!') -> board.save()

  ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\board2.PNG)

  3)  Board.objects.create(title='third', content = 'django')

  * objects를 이용하면 바로 반영된다. (?)

![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\board3.PNG)

​			but, board 치면 다시 -1????? 근데 Board.objects.all() 해보면 잘 들어가 있음. 

![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\board4.PNG)



​			Board.objects.all()  : QuerySet의 형태로 반환

![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\board5.PNG)		



* 유효성 검사 : full_clean()
  * max_length 위반해보기

```
>>> board.title = '아하ㅎ하하하ㅂ아하하하하ㅏ하하핳아아ㅏㅇ'
>>> board.full_clean()
```

![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\board6.PNG)

## 

### 4-2) c'R'ud ( Read )

1. **model.py 수정** 

   def \__str__(self)

   ```python
   # Create your models here.
   class Board(models.Model):
       #CharField : max_length가 필수
       title = models.CharField(max_length=10)
       content = models.TextField()
   
       #auto_now_add=True: '최초 insert'시 언제 작성되었는지
       created_at = models.DateTimeField(auto_now_add=True)
       # 'update', 수정할때마다 변경
       updated_at = models.DateTimeField(auto_now=True)
   
       #########추가#########
       def __str__(self):
           return f'{self.id}번글 - {self.title} : {self.content}'
   
   ```

2. **확인** 

   ```
   from boards.models import Board
   Board.objects.all() # = select * from boards
   ```

   ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\read1.PNG)



3. **조건 검색 (filter, get)**

   * 사전 작업. title이 first인 글 작성

     명령어 : Board.objects.create(title='first',content='hahahah')
     결과 : <Board: 5번글 - first : hahahah>

   1) objects.**filter()**

   * boards = Board.objects.**filter**(title='first')

   * boads 입력해서 확인

     <QuerySet [<Board: 1번글 - first : django>, <Board: 5번글 - first : hahahah>]>

     ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\read3.PNG)

     

   2) objects.**get(pk=1)**

   ​			![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\get.PNG)

   * **.get() 은 1개의 반환값만을 갖기때문에 unique한 값으로 필터할때 사용하도록 한다.**

     ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\get2.PNG)

   3) get 과 filter의 차이

   ​		![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\getfilter.PNG)



4. **함수 사용**
   * board = Board.objects.filter(title='first').first()

![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\read4.PNG)

​		* .first()  /  .last()



5. **정렬(order_by())**
   * 오름차순 : board = Board.objects.**order_by('id').all()**
   * 내림차순 : board = Board.objects.**order_by('-id').all()**



6. **인덱싱 / 슬라이싱**

   * 인덱싱 : board=Board.objects.all()[2]

     ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\index.PNG)

   * 슬라이싱 : board=Board.objects.all()[1:3]

     ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\slicing.PNG)



## 4-3) cr'U'd ( Update )

#### 1. update

​	1) 객체.변수 = '바꿀내용' 

​	2) 객체.save()

```
>>> board = Board.objects.get(pk=1)
>>> board.content='modified!'
>>> board.save()
```

#### ![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\update.PNG)



## 4-4) cru'D' ( Delete )

##### 1) Delete

​	객체.delete()

```
>>> board = Board.objects.get(pk=1)
>>> board.delete()
```

![](C:\Users\multicampus\TIL\190605_Day7_Class_Model_CRUD\imgs\delete.PNG)

​	* 얘는 .save()를 안해도 되네?



## 5. 코드 구현 (Create)

1) views.py

* model의 Board 클래스 import 

```python
from .models import Board
```

* 함수 구현

```python
def create(request):
    title = request.GET.get('title')
    #request.GET는 dict라 .get()을 사용하는 것임
    content = request.GET.get('content')

    #sol1
    #board = Board()
    #board.title = title
    #board.content = content
    #board.save()

    #sol2
    board = Board(title=title, content=content)
    board.save()

    #sol3
    #Board.objects.create(title=title, content=content)

    return render(request, 'boards/create.html')	
```

2) new.html

```html
{% extends 'boards/base.html' %}

{% block body %}
    <h1 class="text-center">NEW</h1>
    <hr>
    <form action="/boards/create/">
    <!--   method의 default는 GET이니까 생략해도 된다.     -->
        <label for="title">Title</label><br>
        <input type="text" name="title" id="title"><br>

        <label for="content">Content</label><br>
        <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
        <input type="submit" value="submit">
    </form>
{% endblock %}
```

3) create.html

```html
{%extends 'boards/base.html'%}

{%block body%}
<p>글이 정상적으로 작성되었습니다.</p>
{%endblock%}
```

4) url.py

```python
from django.contrib import admin
from django.urls import path
from . import views

#작성방향 : 새로운 것이 아래로 ↓
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create)
]
```