1. **새로운 앱 만들기**

   python manage.py startapp utilities

   

2. **등록하기**

```python
# settings.py
INSTALLED_APPS = [
    'utilities',
    'pages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



3. **intro/urls에서 각 앱으로 구분**

```python
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls)

]
```

4. **html 파일들 수정**

   ```html
   <form action="/catch/" method="GET">
       던질거1 : <input type="text" name="message1">
       던질거2 : <input type="text" name="message2">
       <input type="submit" value="submit">
   </form>
   ```



5. **이름 공간의 분리**

views에서 html render를 위해 templates을 뒤질때 installed_apps 순서대로 찾는다.

따라서, pages/index를 해도 동일한 index.html (installed_apps에 먼저 등록된 앱의 index.html)이 나온다.

해결? 

​	1) template에 앱의 이름과 동일한 directory를 더 만들어 준다.

![이름공간분리](.\imgs\4_namespace\directory.PNG)



​	2) 각각 view파일의 함수 render 수정

```python
def index(request):
    return render(request, 'pages/index.html')
```

```python
def index(request):
    return render(request, 'utilities/index.html')
```





1.상속

```python
#setting.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

```python
'DIRS': [os.path.join(BASE_DIR, 'intro', 'templates')],
```



join -> list를 문자열로

기본 경로를 기준으로, intro templates에서 base.html찾아

```html
<!--        base.html        -->

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <h1>장고 연습</h1>
    <hr>
    <div class = 'container'>
        {% block body %}
 <!-- 여기에 이 코드를 상속받을 아이들의 코드가 들어오게될거야! 일종의 template을 만든거징 -->
        {% endblock%}
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

기존의 다른 html에 들어가서 

```html
{% extends 'base.html' %}
{% block body %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>ASCII ART에 오신 것을 환영합니다. ^_________________^</h1>
    <form action="/pages/result/" method="GET">
        영단어를 입력하세요. <input type="text" name="word">
        <input type="submit" value = "submit">
    </form>
</body>
</html>

{% endblock %}
```

결과

![상속](.\imgs\4_namespace\base.PNG)





