import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom"

function Players() {
    const [players, setPlayers] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5555/players')
            .then(resp => resp.json())
            .then(data => setPlayers(data))
    }, [])

    return (
        <div>
            <h1>Current Runescape Players</h1>
            <ol>
                {players.map(player => (
                    <li key={player.id}>
                        <Link to={`/players/${player.id}`}>
                            {player.name} (Combat Level: {player.level})
                        </Link>
                    </li>
                ))}
            </ol>
        </div>
    );
}

export default Players;