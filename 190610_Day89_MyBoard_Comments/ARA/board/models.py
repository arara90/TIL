from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=15);
    content = models.TextField();

    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);

class Comment(models.Model):

    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);

    # verion2 이상에서 on_delete는 필수 인자가 되었다.
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        #foregnKey로 지정한 변수명_id로 보여줌(board_id)
        return f'<Board{self.board_id}: Comment({self.id} - {self.content})>'