# Model Relation

### 1. onetomany (1:N)

project명 : modelrealtion

app명 : onetomany



models.py

```python
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Board(models.Model):
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=20)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'
```



#### Data 입력

1. 

   data : <http://bit.do/onetomany-haha>

   python manage.py shell_plus 후 입력



2. SELECT 연습

   (1) 1번 유저의 모든 게시글

   * user1.board_set.all()

     

   (2) 1번 게시글의 코멘트 중 본인이 쓴 코멘트만.

   * In [15]: for board in user1.board_set.all():
         ...:    for comment in board.comment_set.all():
         ...:        if comment.user == user1:
         ...:            print(comment.content)

     

   (3) 1번 글의 첫번째 댓글을 쓴 사람의 이름

   * board1.comment_set.all()[0].user.name
   * board1.comment_set.first().user.name

   

   (4) 1번 글의 2번째에서 4번째까지 댓글

   * board1.comment_set.all()[1:4]

     

   (5) 1번글의 2번째 댓글을 쓴 사람의 첫번째 게시글

   * board1.comment_set.all()[1].user.board_set.all().first()

   

## 2. many to many (M:N)

1. models.py

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}번 의사 {self.name}'

class Patient(models.Model):
    name = models.CharField(max_length=20)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor}의 환자 {self.patient}'
```



2. SELECT

   (1) doctor에 예약한 환자 목록

   * for reservation in doctor1.reservation_set.all():
         ...:     print(reservation.patient.name)

   

### **3. Many to Many** [  models.ManyToManyField ]

**(1) doctors = models.ManyToManyField(Doctor, through='Reservation')**

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}번 의사 {self.name}'

class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor, through='Reservation')

    def __str__(self):
        return f'{self.id}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor}의 환자 {self.patient}'
```

(2) 모두 가져오기

* patient.doctors.all()     #patient class에서 ManyToManyfield로 지정했으므로 사용할 수 있는 것.

* doctor.patient_set.all() (doctor의 입장)



(3)  역참조 :  **related_name**='patients' (정-역 관계를 지정)

```python
doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
```

이제  doctor.patients.all() 로 가져올 수 있다. ( doctor.patient_set.all()는 더 이상 X )

​	

* **related_name 를 통해  1:N과 구분할 수 있다. ( doctor.patients_set.all() )**
  * **'게시글' 에** 좋아요를 한 유저들
    * 게시글-유저( 1:N  = user.board_set.all() )
    *  좋아요한게시글-유저 ( M:N = user.like_boards )



(4)  이전처럼 직접 Reservation class를 만들지는 않았지만 자동으로 table[manytomany(appname)_patient_doctors]  1개가 더 만들어진것

```python
# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}번 의사 {self.name}'

class Patient(models.Model):
    name = models.CharField(max_length=20)
    #doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    doctors = models.ManyToManyField(Doctor, related_name='patients')

    def __str__(self):
        return f'{self.id}번 환자 {self.name}'

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.doctor}의 환자 {self.patient}'
```



(5) 추가

patient = Patient.objects.get(pk=1)

doctor.patients.**add**(patient )



(6) 삭제

doctor.patients.**remove**(patient ) - 관계삭제 (cf .delete는 record 삭제 )



### 4. Board에 적용해보기

#### **1. models.py**

```python
from django.db import models
from django.conf import settings

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_user', blank=True )

    def __str__(self):
        return f'{self.title} ,{self.content} '

class Comment(models.Model):
    content = models.CharField(max_length=100)
    # USER와 댓글의 1:M 관계 만들기
    # AUTH_USER_MODEL
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ('-pk',)
```



#### 2. views.py

```python
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
```



#### 3. html 모듈화 및 좋아요반영

(1) fontawesome에서 script 가져오기

[https://fontawesome.com](https://fontawesome.com/)



(2) _board.html

```html
<div class="card-body">
    <a href="{% url 'boards:like' board.pk %}" class="card-link">
        {% if user in board.like_users.all %}
            <i class ="fas fa-heart fa-lg" syle="color:crimson">  </i>
        {% else %}
            <i class ="far fa-heart fa-lg" syle="color:black">  </i>
    </a>
    <p class="card-text"> {{ board.like_users.count }} 명이 좋아합니다. </p>
    
</div>
```

(3) index.html

```html
{% extends 'boards/base.html' %}
{% block body %}
<h1 class="text-center">INDEX</h1>
<hr>
    {% for board in boards %}
        <p><b>글 작성자: {{ board.user }}</b></p>
        <p>글 번호: {{ board.pk }}</p>
        <p>글 제목: {{ board.title }}</p>
        <a href="{% url 'boards:detail' board.pk %}">[글 상세보기]</a><br>
        {% include "boards/_board.html" %}
        <hr>
    {% endfor %}

    {% if user.is_authenticated %}
        <a href="{% url 'boards:create' %}">[글 작성]</a>
    {% else %}
        <a href="{% url 'accounts:login' %}">[글을 작성하려면 로그인 해주세요]</a>
    {% endif %}
{% endblock %}
```

