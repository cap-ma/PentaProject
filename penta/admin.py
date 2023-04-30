from django.contrib import admin

from django.contrib import admin
from .models import News,League,Plays,Teams

class imageAdmin(admin.ModelAdmin):

    list_display = ["title",'image_tag']
    
admin.site.register(News, imageAdmin)
admin.site.register(League)
admin.site.register(Plays)
admin.site.register(Teams)


# Register your models here.

