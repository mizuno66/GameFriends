import graphene
from graphene_django import DjangoObjectType
from .models import GameInfos, GameGenres 
 
class GameInfosType(DjangoObjectType):
    class Meta:
        model = GameInfos

class GameGenresType(DjangoObjectType):
    class Meta:
        model = GameGenres
 
class Query(graphene.ObjectType):
    gameInfos = graphene.List(GameInfosType)
    gameInfo = graphene.Field(GameInfosType, id=graphene.Int())
    gameGenres = graphene.List(GameGenresType)
    gameGenre = graphene.Field(GameGenresType, id=graphene.Int())
 
    def resolve_gameInfos(self, info, **kwargs):
        return GameInfos.objects.all()
 
    def resolve_gameInfo(self, info, **kwargs):
        id = kwargs.get('id')
        return GameInfos.objects.get(pk=id)
 
    def resolve_gameGenres(self, info, **kwargs):
        return GameGenres.objects.all()

    def resolve_gameGenre(self, info, **kwargs):
        return GameGenres.objects.get(pk=id)
