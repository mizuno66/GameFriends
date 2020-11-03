from django.db import models

class GameGenres(models.Model):

    class Meta:
        db_table = 'game_genres'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
