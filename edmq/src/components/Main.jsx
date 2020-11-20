import React, { Fragment } from 'react';
import Content from './Content'

const Main = (props) => {

  const images = {
    background: require('../assets/backgroundSplash.jpg')
  };

  return ( 
    <Fragment>
      <img id="background" src={images.background} alt="background"/>
      <div className="App-header">
        <h2>Electronic Dance Music Quiz</h2>
      </div>
      <Content />
    </Fragment>
   );
};
 
export default Main;