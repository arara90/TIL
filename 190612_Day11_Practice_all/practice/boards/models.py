from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

def board_image_path(instance, filename):
    return f'boards/{instance.pk}번글/images/{filename}'


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #image = models.ImageField(blank=True)
    image = ProcessedImageField(
        # 어디로 이미지를 저장할거에요?
        # 우리는 base로 media 폴더를 지정했으므로 그 밑에 boards폴더가 생기고 그 밑에 images폴더
        #source='image',
        upload_to= board_image_path,
        processors= [Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 90 }
    )

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


