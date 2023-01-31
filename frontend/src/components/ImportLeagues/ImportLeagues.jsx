//? How can we go about importing all selected leagues at once, on a single onClick event?

import { useState } from "react";
import axios from 'axios';

const ImportLeagues = () => {
    
    const [selectedLeagues, setSelectedLeagues] = useState([]);

    async function handleImportLeagues() {
        try {
            for (const league of selectedLeagues) {
                const response = await axios.get(`https://api.sleeper.app/v1/league/${league_id}`)
                console.log(response.data)
            }
        } catch (error) {
            console.log(error.message)
        }
    } 
    
    
    return ( 
        <div>
            
        </div>
     );
}
 
export default ImportLeagues;