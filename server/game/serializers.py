from rest_framework import serializers
from game.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            "player",
            "created_at",
            "points_earned",
        ]
