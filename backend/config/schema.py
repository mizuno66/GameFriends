import games.schema
import graphene
import graphql_jwt
from django.dispatch import receiver
from graphql_jwt.refresh_token.signals import refresh_token_rotated


class Query(games.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    @receiver(refresh_token_rotated)
    def revoke_refresh_token(sender, request, refresh_token, **kwargs):
        refresh_token.revoke(request)


schema = graphene.Schema(query=Query, mutation=Mutation)
