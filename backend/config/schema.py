import graphene
from graphene.types import schema
import games.schema

class Query(games.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
