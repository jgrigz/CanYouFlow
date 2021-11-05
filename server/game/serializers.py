from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)
from game.models import Game


class GameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = [
            "player",
            "beat",
            "created_ay",
            "finshed_at",
            "points_earned",
        ]
