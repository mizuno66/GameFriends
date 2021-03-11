/* eslint-disable no-console */
import { useCallback } from 'react';
import { useMutation, gql, ApolloError } from '@apollo/client';

interface Payload {
  username: string;
  exp: number;
  origIat: number;
}

interface TokenAuth {
  tokenAuth: {
    token: string;
    payload: Payload;
    refreshToken: string;
    refreshExpiresIn: number;
  };
}

const TOKEN_AUTH = gql`
  mutation tokenAuth($username: String!, $password: String!) {
    tokenAuth(username: $username, password: $password) {
      token
      payload
      refreshToken
      refreshExpiresIn
    }
  }
`;

// 画面上の入力に使用
export interface Inputs {
  username: string;
  password: string;
}

interface Return {
  authentication: (inputs: Inputs) => Promise<boolean>;
  loading: boolean;
  error: ApolloError | undefined;
}

export const useAuthentication = (): Return => {
  const [tokenAuth, { loading, error }] = useMutation<TokenAuth, Inputs>(
    TOKEN_AUTH,
  );

  const authentication = useCallback(
    async (inputs: Inputs): Promise<boolean> => {
      try {
        const result = await tokenAuth({
          variables: {
            username: inputs.username,
            password: inputs.password,
          },
        });

        if (result.data !== null && result.data !== undefined) {
          localStorage.setItem('token', result.data.tokenAuth.token);
          localStorage.setItem(
            'refreshToken',
            result.data.tokenAuth.refreshToken,
          );
          localStorage.setItem(
            'refreshExoireIn',
            result.data.tokenAuth.refreshExpiresIn.toString(),
          );

          return true;
        }

        return false;
      } catch (autherror) {
        console.error(autherror);

        return false;
      }
    },
    [tokenAuth],
  );

  return { authentication, loading, error };
};
