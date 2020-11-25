import json

from django.http.response import HttpResponse
from games.models.User import User
from graphene_django.utils.testing import GraphQLTestCase


class JWTAuthenticationTestCase(GraphQLTestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(  # type: ignore
            username='testuser',
            email='test@example.com',
            password='secret_password')

    def get_token_query(self, username: str, password: str) -> HttpResponse:

        response = self.query(
            query='''
            mutation tokenAuth($username: String!, $password: String!) {
                tokenAuth(username: $username, password: $password) {
                    token
                    payload
                    refreshToken
                    refreshExpiresIn
                }
            }
            ''', variables={
                'username': username,
                'password': password,
            }
        )

        return response

    def test_tokenAuth(self) -> None:

        response = self.get_token_query("testuser", "secret_password")

        content = json.loads(response.content)

        print(content)

        self.assertResponseNoErrors(response)

    def test_verify(self) -> None:

        response = self.get_token_query("testuser", "secret_password")

        content = json.loads(response.content)

        token: str = str(content["data"]["tokenAuth"]["token"])

        response = self.query(
            '''
            mutation verifyToken($token : String!) {
                verifyToken(token: $token) {
                    payload
                }
            }
            ''', variables={
                'token': token,
            }
        )

        content = json.loads(response.content)

        print(content)

        self.assertResponseNoErrors(response)

    def test_refresh(self) -> None:

        response = self.get_token_query("testuser", "secret_password")

        content = json.loads(response.content)

        refreshToken: str = str(content["data"]["tokenAuth"]["refreshToken"])

        response = self.query(
            '''
            mutation RefreshToken($refreshToken: String!) {
                refreshToken(refreshToken: $refreshToken) {
                    token
                    payload
                    refreshToken
                    refreshExpiresIn
                }
            }
            ''', variables={
                'refreshToken': refreshToken,
            }
        )

        content = json.loads(response.content)

        print(content)

        self.assertResponseNoErrors(response)

    def test_revoke(self) -> None:
        response = self.get_token_query("testuser", "secret_password")

        content = json.loads(response.content)

        refreshToken: str = str(content["data"]["tokenAuth"]["refreshToken"])

        response = self.query(
            '''
            mutation RevokeToken($refreshToken: String!) {
                revokeToken(refreshToken: $refreshToken) {
                    revoked
                }
            }
            ''', variables={
                'refreshToken': refreshToken,
            }
        )

        content = json.loads(response.content)

        print(content)

        self.assertResponseNoErrors(response)

        response = self.query(
            '''
            mutation RefreshToken($refreshToken: String!) {
                refreshToken(refreshToken: $refreshToken) {
                    token
                    payload
                    refreshToken
                    refreshExpiresIn
                }
            }
        ''', variables={
                'refreshToken': refreshToken,
            }
        )
        content = json.loads(response.content)

        self.assertEqual(
            content["errors"][0]["message"],
            "Invalid refresh token")

    def test_refresh_auto_reboke(self) -> None:
        response = self.get_token_query("testuser", "secret_password")

        content = json.loads(response.content)

        refreshToken: str = str(content["data"]["tokenAuth"]["refreshToken"])

        response = self.query(
            '''
            mutation RefreshToken($refreshToken: String!) {
                refreshToken(refreshToken: $refreshToken) {
                    token
                    payload
                    refreshToken
                    refreshExpiresIn
                }
            }
        ''', variables={
                'refreshToken': refreshToken,
            }
        )
        content = json.loads(response.content)

        response = self.query(
            '''
            mutation RefreshToken($refreshToken: String!) {
                refreshToken(refreshToken: $refreshToken) {
                    token
                    payload
                    refreshToken
                    refreshExpiresIn
                }
            }
        ''', variables={
                'refreshToken': refreshToken,
            }
        )
        content = json.loads(response.content)

        self.assertEqual(
            content["errors"][0]["message"],
            "Invalid refresh token")
