import React, { useState } from 'react';
import axios from 'axios';

const SearchGame = () => {
  const [criteria, setCriteria] = useState('');
  const [value, setValue] = useState('');
  const [result, setResult] = useState([]);

  const searchGames = () => {
    axios.get(`http://localhost:5000/api/search?criteria=${criteria}&value=${value}`)
      .then(response => setResult(response.data))
      .catch(error => console.error('Error searching games:', error));
  };

  return (
    <div>
      <h2>Search for Games</h2>
      <label>Criteria: <input type="text" value={criteria} onChange={e => setCriteria(e.target.value)} /></label><br />
      <label>Value: <input type="text" value={value} onChange={e => setValue(e.target.value)} /></label><br />
      <button onClick={searchGames}>Search</button>

      {result.length === 0 ? (
        <p>No matching games found.</p>
      ) : (
        <ul>
          {result.map(game => (
            <li key={game.id}>
              ID: {game.id}, Title: {game.title}, Genre: {game.genre}, Year: {game.year}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default SearchGame;
