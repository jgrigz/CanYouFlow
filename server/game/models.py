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

    def awards(self):
        return f"{self.points_earned} points"

    def __str__(self):
        return f"Game #{self.id} by {self.player.username}"
