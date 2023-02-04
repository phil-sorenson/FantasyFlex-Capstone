import React, { useState, useEffect } from 'react';


const LoginForm = ({ email, password }) => {
    
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    
    const handleSubmit = (event) => {
        event.preventDefault();
        onLogin({email, password});
    };
    
    return ( 
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor='email'>Email: </label>
                <input
                    type='email'
                    id='email'
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                />
            </div>
            <div>
                <label htmlFor='password'>Password</label>
                <input
                    type='password'
                    id='password'
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                />
            </div>
            <button type='button'>Login</button>
        </form>
       
     );
}
 
export default LoginForm;