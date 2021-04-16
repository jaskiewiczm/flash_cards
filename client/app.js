import React from 'react';
import { Switch, BrowserRouter as Router, Route } from 'react-router-dom';

import FlashCard from './components/flash_card'

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/" component={FlashCard} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;