import React, { FC } from 'react';
import { Redirect, Route, Switch, RouteComponentProps } from 'react-router';
import Login from 'components/templates/Login';
import MyPage from 'components/templates/MyPage';

const Characters: FC<RouteComponentProps> = ({ match }) => (
  <>
    <header>
      <h1>Account</h1>
    </header>
    <Switch>
      <Route exact path={`${match.path}/login`}>
        <Login />
      </Route>
      <Route exact path={`${match.path}/mypage`}>
        <MyPage />
      </Route>
      <Redirect to="/" />
    </Switch>
  </>
);
export default Characters;
