/* eslint-disable no-console */
import React, { useEffect, useState } from 'react';
import { useVerify } from 'hooks/useVerify';

const MyPage: React.FC = () => {
  const [username, setUsername] = useState('');
  const { verify, loading, error } = useVerify();

  useEffect(() => {
    let unmounted = false;

    void (async () => {
      const name = await verify();
      console.log(name);
      if (name !== '' && !unmounted) {
        setUsername(name);
      }
    })();

    // クリーンアップ関数を返す
    return () => {
      unmounted = true;
    };
  }, [verify]);

  if (loading) return <p>Loading...</p>;

  return (
    <div>
      {error ? <p>認証エラー</p> : null}
      {username}
      <input type="mail" />
    </div>
  );
};

export default MyPage;
