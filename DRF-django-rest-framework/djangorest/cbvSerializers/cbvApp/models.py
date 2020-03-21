# Create your models here.
from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=11, decimal_places=3)

    def __str__(self):
        return str(self.id) + self.name + str(self.score)
