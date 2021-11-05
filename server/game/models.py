from django.db import models

# models
from authentication.models import CustomUser
from beat.models import Beat


class Game(models.Model):
    player = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.CASCADE
    )
    beat = models.ForeignKey(
        Beat, null=True, blank=True, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField()
    points_earned = models.IntegerField()

    def __str__(self):
        return self.player

    def duration(self):
        return self.created_at - self.finished_at
