1. **shell_plus**

   : 자동으로 from boards.models import Board 요 작업해줌. 

   pip install django_extensions

   * settings.py : INSTALLED_APPS = django_extensions' 추가

   * ```python
     INSTALLED_APPS = [
         'board',
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'django_extensions',
     ]
     ```

2. **comment** 

![](.\imgs\7_Comment\comment1.PNG)



3. **board.comment_set.all()**

   하면 현재 글에 있는 모든 comment를 볼 수 있다.

   comment에서 board를 볼때는 comment.board.title 요론식으로 볼 수 있따.

   반대는 안됨. 1:N?    

   

4. **admin 계정 만들기**

   python manage.py createsuperuser