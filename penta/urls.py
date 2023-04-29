from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from .views import uploadView

urlpatterns = [

    path('admin/', admin.site.urls),
   
    path("upload_news_by_admin/",uploadView,name='upload_image')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
