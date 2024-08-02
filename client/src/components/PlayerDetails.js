import React, { useEffect, useState } from 'react';
import { useParams, useHistory } from 'react-router-dom';

function PlayerDetails() {
    const { id } = useParams();
    const history = useHistory();
    const [player, setPlayer] = useState(null);
    const [name, setName] = useState('');
    const [level, setLevel] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchPlayer();
    }, [id]);

    const fetchPlayer = () => {
        fetch(`http://127.0.0.1:5555/players/${id}`)
            .then(resp => resp.json())
            .then(data => {
                if (data.error) {
                    setError(data.error);
                } else {
                    setPlayer(data);
                    setName(data.name);
                    setLevel(data.level);
                }
            })
    };

    const handleUpdate = (e) => {
        e.preventDefault();

        fetch(`http://127.0.0.1:5555/players/${id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, level })
        })
            .then(resp => resp.json())
            .then(data => {
                if (data.error) {
                    setError(data.error);
                } else {
                    fetchPlayer(); 
                }
            })
    };

    const handleDelete = () => {
        fetch(`http://127.0.0.1:5555/players/${id}`, {
            method: 'DELETE',
        })
            .then(resp => resp.json())
            .then(data => {
                if (data.error) {
                    setError(data.error);
                } else {
                    history.push('/players'); 
                }
            })
    };

    if (error) return <h1>{error}</h1>;
    if (!player) return <h1>Loading....</h1>;

    return (
        <div>
            <h2>Adventurer: {player.name}</h2>
            <h2>Level: {player.level}</h2>

            <h3>Update Player Details</h3>
            <form onSubmit={handleUpdate}>
                <div>
                    <label htmlFor="name">Name:</label>
                    <input
                        type="text"
                        id="name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="level">Level:</label>
                    <input
                        type="number"
                        id="level"
                        value={level}
                        onChange={(e) => setLevel(e.target.value)}
                    />
                </div>
                <button type="submit">Update Player</button>
            </form>

            <button onClick={handleDelete}>Delete Player</button>

            <div>
                {player.player_quests && player.player_quests.length > 0 ? (
                    player.player_quests.map(pq => (
                        <div key={pq.id}>
                            <h3>Quest: {pq.quest?.name || 'No name'}</h3>
                            <p>Progress: {pq.progress}</p>
                        </div>
                    ))
                ) : (
                    <p>No quests available</p>
                )}
            </div>
        </div>
    );
}

export default PlayerDetails;