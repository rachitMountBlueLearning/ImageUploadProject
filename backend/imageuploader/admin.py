from django.contrib import admin
from imageuploader.models import Image

# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo']