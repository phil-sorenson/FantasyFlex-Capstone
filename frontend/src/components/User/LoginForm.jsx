// Handling the platform selection and

import React, { useState, useEffect } from 'react';
import Login from './Login';
import axios from 'axios'
import { useNavigate } from 'react-router-dom';

const LoginForm = ({ signal }) => {

    const navigate = useNavigate();
    
    const initialFormState = {
        username: '',
        password: '',
    }

    const [userInput, setUserInput] = useState(initialFormState);
 
    function handleChange(e) {
        setUserInput({...userInput, [e.target.value]: e.target.value });
    }


    async function handleSubmit(e) {
        e.preventDefault();
        try {
            const authResponse = await signal(userInput); 
            setUserInput(initialFormState)
            
        } catch (error) {
            console.log(error.message)
            navigate('/', {replace: true})
        }
    }

    return ( 
        <form onSubmit={handleSubmit} class-className='login-form'>
            <div>
                <label htmlFor='username'>Username: </label>
                <input
                    type='text'
                    id='username'
                    placeholder='Sleeper Username'
                    value={userInput.username}
                    onChange={handleChange}
                />
            </div>
            <div>
                <label htmlFor='password'>Password</label>
                <input
                    type='password'
                    id='password'
                    placeholder='********'
                    value={userInput.password}
                    onChange={handleChange}
                />
            </div>
            <button type='button'>Login</button>
        </form>
       
     );
}
 
export default LoginForm;