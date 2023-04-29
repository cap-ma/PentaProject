from rest_framework import serializers

from .models import Teams,League,News,Plays

class PlaysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plays
        exclude=['id']


