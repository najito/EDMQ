import React, { Fragment } from 'react';
import Content from './Content';

const Main = (props) => {
  return ( 
    <Fragment>
      <div className="App-header">
        <h2>Electronic Dance Music Quiz</h2>
      </div>
      <Content />
    </Fragment>
   );
};
 
export default Main;