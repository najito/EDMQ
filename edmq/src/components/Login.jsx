import React from 'react';

const Login = () => {
  return ( 
    <div id='login'>
      <form id='loginForm'>
          <div className='loginGroup'>
            <label className='loginLabel'>Username</label>
            <input type='text' placeholder='username' className='loginForm'/>
          </div>
          <div className='loginGroup'>
            <label className='loginLabel'>Password</label>
            <input type='password' placeholder='password' className='loginForm'/>
          </div>
        <input type='submit' value='Login' id='submit'/>
      </form>
    </div>
   );
}
 
export default Login;