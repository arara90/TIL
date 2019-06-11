from django.contrib import admin
from .models import Board, Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')

# models.py에 등록한 Board 클래스 호출
admin.site.register(Board, BoardAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'updated_at')

admin.site.register(Comment, CommentAdmin)