# django - Relationship

1. **ORM**?
2. **one-to-one** : OneToOneField
3. **one-to-many** - ForeignKey
4. **many-to-many** -ManyToManyField



## ORM

##### ORM? (Object-Relational Mapping)

* 객체와 관계형 데이터베이스의 데이터를 매핑해주는 것
* 객체 간의 관계를 바탕으로 SQL 자동 생성해서 sql 쿼리문 없이 db의 데이터들을 다룰 수 있다.



#### queryset 특징

* Lazy : 미리 db에 접근해서 값을 불러오는게 아니라, 출력 등과 같이 필요한 순간에 sql로 매핑되고, 이를 통해 db에 접근해 값을 가져옴

  출처 : [[Django] 데이터베이스 조회, queryset](https://ssungkang.tistory.com/entry/Django-데이터베이스-조회-queryset)

  

## One-to-One

https://django-orm-cookbook-ko.readthedocs.io/en/latest/one_to_one.html

[case] 생부와 생모는 각각 1명씩만 갖는다.

```
from django.contrib.auth.models import User

class UserParent(models.Model):
	user = models.OneToOneField(
		User,
		on_delete = models.CASCADE,
		primary_key = True,
	)
	
	father = models.CharField(max_length=100)
	mother = models.CharField(max_length=100)
	
	
```

user.userparent

userparent.user



## One-to-Many

[case] 하나의 게시글에 달린 댓글들



#### ForeignKey

* 댓글(N) object의 post field에 **ForeignKey**설정

```
class Post(models.Model):
  # 생략
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
```

comment.post

post.comment_set.all()  : 당하는 입장에서는 set이 필요. (ManyToManyField도 같음)



* **on_delete**

  * CASCADE : 연결되어 있는 N쪽의 데이터 함께삭제

  * PROTECT : ForeignKey로 연결된 1쪽의 데이터가 삭제되지 않도록 보호

  * SET_NULL : null로 대체, null=True 옵션 필요

  * SET_DEFAULT : default값으로 대체, default=True 필요

  * SET: 대체할 값이나 함수 지정

  * DO_NOTHING : 아무것도 안함, db오류 발생 가능

    

* **limit_choices_to** = { 'field명' : value }

  * Post(**1**:N 에서 **1** 쪽에) 모델에 필드 조건 주기.

  ​    주로 1쪽(하나의 POST)에서 N(딸린 댓글들)을 검색하게 되는 상황이 많으니까 상황을 기억하자.

  ```
  class Comment(models.Model):
    post = models.ForeignKey(
      Post,
      on_delete=models.CASCADE,
    	limit_choices_to = {'is_published': True},
    )
  ```

  ```sql
  select *
  from Post INNER JOIN Comment
  on Post.id = Comment.id
  and Post.is_published = 'True'
  ```
  

  * callable 폼을 사용하는 예제 (https://brunch.co.kr/@ddangdol/5)

  ```python
  def limit_pub_date_choices():
  	return {'pub_date_lte' : datetime.date.utcnow()}
  
  limit_choices_to = limit_pub_date_choices
  ```

  단, 새로운 폼이 instance화 될때마다, 유효성 검증 시 마다 호출된다. admin은 다양한 케이스의 폼입력의 유효성을 여러번 검증하기 위해 쿼리셋을 구성하기 때문에 callable이 여러 번 호출될 수 있으므로 주의하자.

  

*아.. 그냥 쿼리로 하고싶다...ㅋㅋㅋㅋㅋㅋ*



* ForeignKey.**to_field** : 기본적으로 django는 기본키를 사용하지만, 다른 필드를 참조하고 싶을때 사용한다. 다만, 해당 필드는 반드시 unique = True여야 한다.



* ForeignKey.**swappable** : ....? 이해 못했다.  사용자 정의 user 모델이 예로 나와있어서 짚고 넘어가야하겠지만, 일단 pass하자.

### Many-to-Many

[수업참고 : TIL_django/K_Model_Relation.md](https://github.com/arara90/TIL_django/blob/master/K_Model Relation.md)

종합병원의 doctor - patient 관계 M:N



#### ManyToManyField

```
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

1. 한쪽에 ManyToManyField를 걸어주고, through를 통해 M:N 관계에 의해 생성될 테이블 따로 지정해줄 수 있다 (지정하지 않아도 자동으로 만들어짐)

2. M:N 관계에 의해 만들어진 테이블에는 각각을 ForeignKey로.

    (M:N관계를 그리면 당연하게 연상이 될 것이다.)

3. 이 경우에 patient에서 ManyToManyField를 정의했으니까 

   ```
   patient.dotors.all()
   doctor.patient_set.all() 
   ```

4. **related_name**

* 역참조 (정-역관계 지정)

  ```
  doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
  ```

  이렇게 지정하면, doctor에서도 related_name을 통해 역참조를 쉽게 할 수 있다.

  ```
  patient.dotors.all()
  doctor.patients.all() 
  ```

* 참고로 related_name = '+' 는  역방향 관계를 갖지 않도록 보장한다.







### 더 공부하기

https://brunch.co.kr/@ddangdol/5



