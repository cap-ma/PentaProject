from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

from .views import uploadView,get_leagues,get_matches,sort_teams_by_score,get_news_by_id,get_news_all

urlpatterns = [

   
   
    #path("api/v1/upload_news_by_admin/",uploadView,name='upload_image'),
    path("api/v1/get_all_league",get_leagues,name="all_leagues"),
    path("api/v1/get_matches_by_league/<int:id>",get_matches,name="get_match_by_league"),
    path("api/v1/sort_teams/<int:id>",sort_teams_by_score,name="sort_teams"),
    path("api/v1/get_news_by_id/<int:id>",get_news_by_id,name='a_news'),
    path("api/v1/get_news_all",get_news_all,name='news')
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
