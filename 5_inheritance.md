1.**상속**

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
##여기에서 DIRS를 다음과 같이 수정하면!
```

```python
'DIRS': [os.path.join(BASE_DIR, 'intro', 'templates')],
#join -> list를 문자열로
# 기본 경로(BASE_DIR)를 기준으로, intro templates에서 base.html찾아
```



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

    <h1>ASCII ART에 오신 것을 환영합니다. ^_________________^</h1>
    <form action="/pages/result/" method="GET">
        영단어를 입력하세요. <input type="text" name="word">
        <input type="submit" value = "submit">
    </form>

{% endblock %}
```

결과

![상속](.\imgs\5_inheritance\base.PNG)

![](.\imgs\5_inheritance\\dev2.PNG)





