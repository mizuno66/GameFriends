import React from 'react';
import { Route, Switch } from 'react-router';
import { Link } from 'react-router-dom';
import logo from './assets/img/logo.svg';
import './assets/css/App.css';
import Account from './components/pages/Account';

const App: React.FC = () => (
  <Switch>
    <Route exact path="/">
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.tsx</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          <Link to="/Account/login">ログイン</Link>
        </header>
      </div>
    </Route>
    <Route path="/Account" component={Account} />
  </Switch>
);

export default App;
