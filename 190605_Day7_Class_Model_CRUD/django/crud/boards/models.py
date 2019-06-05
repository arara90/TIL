from django.db import models

# Create your models here.
class Board(models.Model):
    #CharField : max_length가 필수
    title = models.CharField(max_length=10)
    content = models.TextField()

    #auto_now_add=True: '최초 insert'시 언제 작성되었는지
    created_at = models.DateTimeField(auto_now_add=True)
    # 'update', 수정할때마다 변경
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content}'





