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
    game_infos = graphene.List(GameInfosType)
    game_info = graphene.Field(GameInfosType, id=graphene.Int())
    game_genres = graphene.List(GameGenresType)
    game_genre = graphene.Field(GameGenresType, id=graphene.Int())

    def resolve_game_infos(self, info, **kwargs):
        return GameInfos.objects.all()

    def resolve_game_info(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return GameInfos.objects.get(pk=id)

        return None

    def resolve_game_genres(self, info, **kwargs):
        return GameGenres.objects.all()

    def resolve_game_genre(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return GameGenres.objects.get(pk=id)

        return None
