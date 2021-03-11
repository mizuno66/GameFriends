/* eslint-disable no-console */
import { useCallback } from 'react';
import { useMutation, gql, ApolloError } from '@apollo/client';

interface Payload {
  username: string;
  exp: number;
  origIat: number;
}

interface VerifyToken {
  verifyToken: {
    payload: Payload;
  };
}

interface Args {
  token: string;
}

interface Return {
  verify: () => Promise<string>;
  loading: boolean;
  error: ApolloError | undefined;
}

const VERIFY_TOKEN = gql`
  mutation verifyToken($token: String!) {
    verifyToken(token: $token) {
      payload
    }
  }
`;

// eslint-disable-next-line import/prefer-default-export
export const useVerify = (): Return => {
  const [verifyToken, { loading, error }] = useMutation<VerifyToken, Args>(
    VERIFY_TOKEN,
  );

  const verify = useCallback(async (): Promise<string> => {
    const t = localStorage.getItem('token');
    console.log(t);
    if (t === null) return '';

    const payload = await verifyToken({
      variables: {
        token: t,
      },
    });

    if (payload.data !== undefined && payload.data !== null) {
      console.log(payload.data);

      return payload.data.verifyToken.payload.username;
    }

    return '';
  }, [verifyToken]);

  return { verify, loading, error };
};
