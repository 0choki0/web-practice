from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


# Create your models here.
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[300,300],
        crop=['middle', 'center'],
        upload_to='profile'
        )

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)

