import React, { useState } from 'react';
import axios from 'axios';

const AddGame = () => {
  const [title, setTitle] = useState('');
  const [genre, setGenre] = useState('');
  const [year, setYear] = useState('');

  const addGame = () => {
    axios.post('http://localhost:5000/api/add', { title, genre, year })
      .then(response => console.log('Game added successfully.'))
      .catch(error => console.error('Error adding game:', error));
  };

  return (
    <div>
      <h2>Add a New Game</h2>
      <label>Title: <input type="text" value={title} onChange={e => setTitle(e.target.value)} /></label><br />
      <label>Genre: <input type="text" value={genre} onChange={e => setGenre(e.target.value)} /></label><br />
      <label>Year: <input type="text" value={year} onChange={e => setYear(e.target.value)} /></label><br />
      <button onClick={addGame}>Add Game</button>
    </div>
  );
};

export default AddGame;
