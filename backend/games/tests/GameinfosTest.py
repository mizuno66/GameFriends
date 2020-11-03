import json
from graphene_django.utils.testing import GraphQLTestCase
from games.models import GameInfos
from games.models import GameGenres

class GameinfosTestCase(GraphQLTestCase):
    def setUp(self) -> None:
        GameGenres.objects.create(id=1, name="テストゲームジャンル")
        GameInfos.objects.create(id=1, name="テストゲーム情報", game_genre=GameGenres.objects.get(pk=1))

    def test_some_query(self) -> None:
        response = self.query(
            '''
            query {
                gameInfos {
                    id
                    name
                }
            }
            '''
        )

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)

        print(content)

    def test_relation(self) -> None:
        response = self.query(
            '''
            query {
                gameInfos {
                    id
                    name
                    gameGenre{
                        id
                        name
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)

        print(content)

        self.assertResponseNoErrors(response)
