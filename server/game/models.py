from django.db import models

# models
from authentication.models import CustomUser


class Game(models.Model):
    player = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.CASCADE
    )
    # beat = models.ForeignKey(
    #     Beat, null=True, blank=True, on_delete=models.CASCADE
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    points_earned = models.IntegerField()

    def __str__(self):
        return self.player
