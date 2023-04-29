from django.contrib import admin

from django.contrib import admin
from .models import News

class imageAdmin(admin.ModelAdmin):

    list_display = ["title",'image_tag']

admin.site.register(News, imageAdmin)

# Register your models here.
