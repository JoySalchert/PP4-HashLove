from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, related_name='user_info', null=False)
    bio = models.TextField('Bio', blank=True, null=True, default=None)
    