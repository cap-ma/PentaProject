from rest_framework import serializers

from .models import Teams,League,News,Plays

class PlaysSerializer(serializers.ModelSerializer):

    class Meta:
        model=Plays
        fields='__all__'

   
    

class LeagueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=League
        
        fields='__all__'


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teams
        fields='__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','title','image','text','date')

        