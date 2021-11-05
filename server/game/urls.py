from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from game.views import CreateGameView, GamesView


#  using regex so it will ONLY work at localhost 5000
url_patterns = [
    path("cyf-start-game/", CreateGameView.as_view()),
    path("cyf-all-games/", GamesView.as_view())
]