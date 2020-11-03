from django.db import models
from .GameGenres import GameGenres

class GameInfos(models.Model):
    
    class Meta:
        db_table = 'game_infos'

    name = models.CharField(max_length=50)
    game_genre = models.ForeignKey(GameGenres, related_name="related_info_genres", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
