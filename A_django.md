# Django

1. Static vs **Dynamic web**

   * Static : 이미 정해진 방식의 response를 주는 것

   * Dynamic : 유저의 Input에 따라 다른 reponse를 제공

     

2.  Framework

3. Flask ?

   *  Micro Web Framework
   * 보안에 취약

4. **동작방법** : **MTV** (vs MVC) pattern

   * Model (Data 관리) / models.py
   * Template (사용자가 보는 화면) / 
   * View (중간관리자 - 요청들어오면 어떤 데이터를 보여줄까) / urls.py , views.py

   * mvc  -> model, view, controller

------

**오늘의 주제 : ** M**VT**

요청 보내면 중간관리자가 어떤 데이터(함수)를 보여줄지 결정하고 보여주자.

1. **설치 및 project 생성**

   1) 설치 및 project 생성

   ```
   pip install django
   django-admin startproject intro
   ```

   2) gitignore.io 에 django 생성 후 cntl + a , .gitignore 파일에 cntl + v 

   3) intro로 이동 , manage.py 확인 -> 서버실행 및 앱 생성 

   ```
    #서버실행
    python manage.py runserver
    
    #pages앱 생성 => pages directory 생성된다.
    python manage.py startapp pages
   ```

* migrations : 일종의 설계서 저장



2. **설정**

   1) app 등록하기. 

   ​	intro > settings.py 

   ```python
   INSTALLED_APPS = [
       'pages',
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   
   LANGUAGE_CODE = 'ko-kr'
   TIME_ZONE = 'Asia/Seoul'
   ```



2. **주요 기능 파일 (3대장)**

   **urls.py** - 요청 url과의 연결 (flask - app.route에 썼던걸 여기에 저장)

   **views.py** - url에 연결되어 실행될 함수 (flask - app.route 밑에 있던 함수, 					context에 필요 정보 담아 로드할 html 주소에 연결. 

   **models.py** - DB 연동(data 관리)

   

   주소요청 -> urls -> views -> 작업실행 ->  보여줄 html

   

   1) urls.py

   ```python
   ## views 파일 추가
   from pages import views
   
   #path( user가 요청한 'urlpattern/', 실행할 def) 
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('index/', views.index),
       path('hola/', views.hola),
       path('dinner/', views.dinner),
       path('hello<str:name>/', views.hello),
       path('introduce/<name>/<int:age>', views.introduce),
       # str이 default이므로 <name>도 가능
       # path('hello<name>/', views.hello),
   ]
   
   ```

   2) views.py

   ```python
   from django.shortcuts import render
   import random
   
   # Create your views here.
   def index(request):
       return render(request, 'index.html')
   
   def hola(request):
       return render(request, 'hola.html')
   
   def dinner(request):
       menu = ['족발', '삼겹살', '냉면', '치맥', '피자', '양고기', '다이어트!!!!']
       pick = random.choice(menu)
       context = {'pick':pick}
       #return render(request, 'dinner.html', {'pick': pick})
       return render(request, 'dinner.html', context)
   
   def hello(request, name):
       context = {'name': name}
       return render(request, 'hello.html', context)
   
   def introduce(request, name, age):
       context = {'name': name , 'age': age}
       return render(request, 'introduce.html', context)
   ```

   3) pages > templates 디렉토리 만들고 내부에 html 파일 만들기 (index.html)

   ​	: 장고는 기본적으로 이 주소안에 있는 html을 렌더한다.

   ```html
   <!-- introduce.html -->
   <h1> 내 이름은 {{ name }}, 나이는 {{ age }} </h1>
   ```

   

   4) http://127.0.0.1:8000/index/ 접속