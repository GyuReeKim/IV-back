from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# 유저
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")


# 유저 프로필
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)

    def __str__(self):
        if self.nickname == "":
            return self.user.username
        else:
            return f'{self.user.username} ({self.nickname})'


# 유저 생성 시 유저 프로필 생성
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# 유저 프로필 저장
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()