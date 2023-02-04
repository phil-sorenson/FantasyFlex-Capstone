import React, { useState, useEffect } from 'react';

const LoginForm = () => {
    
    const [platform, setPlatform] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    
    const handleSubmit = async (event) => {
        event.preventDefault();

        const data = {platform, username, password}
    }
    
    return ( 
        <form onSubmit={handleSubmit}>
            <select value={platform} onChange>

            </select>
        </form>
       
     );
}
 
export default LoginForm;