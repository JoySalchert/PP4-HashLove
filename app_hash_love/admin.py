from django.contrib import admin
from .models import UserInfo

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass

# Register your models here.
