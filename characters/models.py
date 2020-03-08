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