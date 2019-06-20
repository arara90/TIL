from django.db import models
from django.conf import settings

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # USER와 게시글의 1:M 관계 만들기
    # AUTH_USER_MODEL
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