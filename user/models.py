from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):

    class Meta:
        db_table = "my_user" # 여기는 테이블 이름이에요! 꼭 기억 해 주세요!

    bio = models.TextField(max_length=500, blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')