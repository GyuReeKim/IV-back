import os
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.

# 이미지 덮어쓰기
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Character(models.Model):
    name = models.CharField(max_length=50)
    another_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="character", null=True, blank=True, storage=OverwriteStorage())
    explanation = models.TextField()
    difficulty = models.CharField(max_length=50, null=True, blank=True) # 난이도 # 컨트롤 난이도가 높습니다.
    
    def __str__(self):
        return f'{self.name} ({self.another_name})'


class Position(models.Model):
    position_name = models.CharField(max_length=50)
    position_grade = models.CharField(max_length=50)
    position_role = models.TextField()

    def __str__(self):
        return f'{self.position_name} - {self.position_grade}'


class Persona(models.Model):
    persona_sort = models.CharField(max_length=50)
    persona_name = models.CharField(max_length=50)
    persona_direction = models.IntegerField() # 몇시 인격
    persona_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    persona_point = models.IntegerField()
    persona_explanation = models.TextField()
    persona_opinion = models.TextField(null=True, blank=True) # 인격에 대한 의견 (사용할 지 고민)

    def __str__(self):
        return f'{self.persona_name} - {self.persona_point}'