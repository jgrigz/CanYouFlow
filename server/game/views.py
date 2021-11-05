from rest_framework import generics

# serializers 
from game.serializers import GameSerializer

# models
from game.models import Game


class CreateGameView(generics.CreateAPIView):
    '''create new user'''
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GamesView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer