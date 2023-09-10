from django.contrib import admin
from .models import UserInfo
from django_summernote.admin import SummernoteModelAdmin

@admin.register(UserInfo)
class UserInfoAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# Register your models here.
