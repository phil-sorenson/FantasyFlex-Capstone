// User is given an array of different platforms in the form of a button/Link --> Once platform is selected, user will be prompted to submit 'email' and 'password' 
    // After login we want to fetch the user's 'user_id' and or 'username' in order to use it in the 'LeagueSelection' component
'use-strict'

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import LoginForm from './LoginForm';



const Login = ({ onLogin }) => {
    
 
    const [userID, setUserID] = useState(null)
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const platforms = [
        {id: 1, name: `Sleeper`, endpoint: `https://api.sleeper.app/v1/user/${username}`}
    ];

    function handlePlatformSelection(platform) {
        setSelectedPlatform(platform);
    }

    async function handleLogin(username,password){
       setIsLoading(true);
        await axios.post(`${selectedPlatform.endpoint}`, {
            username, 
            
        })
        
        .then((response) =>{
            setUserID(`${response.data.user_id}`);
            history.push('/league-selection');
            setIsLoading(false)
        })
        .catch((error) => {
            console.log(error.message)
            setIsLoading(false)
        })
    }
 
    
    return ( 
        <div>
            <LoginForm
                platforms={platforms}
                selectedPlatform={selectedPlatform}
                setSelectedPlatform={setSelectedPlatform}
                isLoading={isLoading}
                handleLogin={handleLogin}
            />
        </div>
     );
}
 
export default Login;