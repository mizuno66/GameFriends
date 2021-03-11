/* eslint-disable no-console */
import { useForm } from 'react-hook-form';
import { useHistory } from 'react-router-dom';
import React, { FC, useEffect } from 'react';
import { Inputs, useAuthentication } from 'hooks/useAuthentication';

const Login: FC = () => {
  const history = useHistory();

  // eslint-disable-next-line @typescript-eslint/unbound-method
  const {
    register,
    handleSubmit,
    reset,
    errors,
    formState: { isSubmitSuccessful },
  } = useForm<Inputs, React.BaseSyntheticEvent>();

  const { authentication, loading, error } = useAuthentication();

  const onSubmit = async (input: Inputs, e?: React.BaseSyntheticEvent) => {
    if (e !== undefined) e.preventDefault();
    const canAuthenticated = await authentication(input);

    if (canAuthenticated) {
      history.push('/Account/mypage');
    } else {
      history.push('/Account/login');
    }
  };

  useEffect(() => {
    if (isSubmitSuccessful) {
      reset({ username: '', password: '' });
    }
  }, [isSubmitSuccessful, reset]);

  if (loading) return <p>Loading...</p>;

  return (
    <div>
      {error ? <p>認証エラー</p> : null}
      <form onSubmit={handleSubmit(onSubmit)}>
        <input
          name="username"
          placeholder="username"
          ref={register({ required: true })}
        />
        {errors.username && <span>ユーザ名を入力してください。</span>}
        <input
          type="password"
          name="password"
          placeholder="password"
          ref={register({ required: true })}
        />
        {errors.password && <span>パスワードを入力してください。</span>}
        <input type="submit" />
      </form>
    </div>
  );
};

export default Login;
