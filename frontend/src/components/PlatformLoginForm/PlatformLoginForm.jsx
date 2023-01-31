import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { Redirect } from 'react-router-dom';

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SleeperLeagues = () => {
  const [leagues, setLeagues] = useState([]);
  const [selectedLeagues, setSelectedLeagues] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchLeagues();
  }, []);

  const fetchLeagues = async () => {
    setLoading(true);
    const response = await axios.get(`/sleeper/leagues`);
    setLeagues(response.data);
    setLoading(false);
  };

  const handleSelect = (league) => {
    setSelectedLeagues([...selectedLeagues, league]);
  };

  const importLeagues = async () => {
    setLoading(true);
    const response = await axios.post(`/sleeper/import`, {
      selectedLeagues,
    });
    setLoading(false);
    // handle response data as needed
  };

  return (
    <div>
      {loading && <p>Loading...</p>}
      {leagues.map((league) => (
        <div key={league.id}>
          <input
            type="checkbox"
            checked={selectedLeagues.includes(league)}
            onChange={() => handleSelect(league)}
          />
          {league.name}
        </div>
      ))}
      <button onClick={importLeagues}>Import Selected Leagues</button>
    </div>
  );
};

export default SleeperLeagues;
