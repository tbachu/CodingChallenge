import React, { useState } from 'react';
import './App.css';

function App() {
    const [userId, setUserId] = useState('');
    const [dishes, setDishes] = useState([]);
    const [page, setPage] = useState(0);

    const fetchDishes = async () => {
    const res = await fetch(`http://127.0.0.1:5000/dishes?userId=${userId}&page=${page}`);
    const data = await res.json();
    setDishes(data);
  };
  
  return (
    <div>
        <input
            value = {userId}
            onChange = {(e) => setUserId(e.target.value)}
            placeholder = "Enter User ID"
        />
        <button onClick={fetchDishes}>Fetch Dishes</button>
        <table>
            <thead>
                <tr>
                    <th>Dish Name</th>
                </tr>
            </thead>
            <tbody>
                {dishes.map((dish, index) => (
                    <tr key={index}>
                        <td>{dish}</td>
                    </tr>
                ))}
            </tbody>
        </table>
        <button onClick={() => setPage(p => Math.max(0, p-1))}>Previous</button>
        <button onClick={() => setPage(p => p+1)}>Next</button>
    </div>
    );
    }

export default App;
