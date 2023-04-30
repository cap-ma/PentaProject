from django.shortcuts import render, redirect # new
from .models import Image,League,Teams,Plays,News

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json 
from rest_framework.response import Response

from .serializer import LeagueSerializer,PlaysSerializer,TeamsSerializer,NewsSerializer

def uploadView(request):                                      
    if request.method == 'POST':
        form = NewsSerializer(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return Response("OK")
    else:
            form = NewsSerializer()
            
    return Response("bad")


def upload_news_admin(request):
     return render(request,'index.html')


@csrf_exempt
@api_view(('GET',))
def get_leagues(request):
      all_leagues=League.objects.all()
      serialized_all_leagues=LeagueSerializer(all_leagues,many=True)
      
      return Response(serialized_all_leagues.data)


@csrf_exempt
@api_view(('GET',))
def get_matches(request):
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        league_id=body["id"]

        matches_by_id=Plays.objects.filter(leag=league_id)
        matches=PlaysSerializer(matches_by_id,many=True)

        return Response(matches.data)

@csrf_exempt
@api_view(('GET',))
def sort_teams_by_score(request):
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        league_id=body["id"]


        sorted_teams=Teams.objects.raw("SELECT * FROM penta_teams WHERE leag_id = %s ORDER BY score DESC , goals_scored-goals_lost DESC",[league_id])

        context=TeamsSerializer(sorted_teams,many=True)
        
        
        
        return Response(context.data)

  
@csrf_exempt
@api_view(('GET',))
def get_news_by_id(request):
        
        body_unicode = request.body.decode('utf-8')

        body = json.loads(body_unicode)
        
        league_id=body["id"]
        
        news=News.objects.filter(id=league_id).first()
        
        news_serializered=NewsSerializer(news)
        print(news_serializered)
        print(news_serializered.data)
        

        return Response(news_serializered.data)

@csrf_exempt
@api_view(('GET',))
def get_news_all(request):
        
      
        
        
        news=News.objects.all()
        
        news_serializered=NewsSerializer(news,many=True)
        
        

        return Response(news_serializered.data)

       