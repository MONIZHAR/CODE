import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GameList = () => {
  const [games, setGames] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/games')
      .then(response => setGames(response.data))
      .catch(error => console.error('Error fetching games:', error));
  }, []);

  return (
    <div>
      <h2>All Games</h2>
      {games.length === 0 ? (
        <p>No games saved.</p>
      ) : (
        <ul>
          {games.map(game => (
            <li key={game.id}>
              ID: {game.id}, Title: {game.title}, Genre: {game.genre}, Year: {game.year}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default GameList;
