from django.contrib import admin
from .models import Placeholder_Model
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Placeholder_Model)
class Placeholder_ModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

# Register your models here.
