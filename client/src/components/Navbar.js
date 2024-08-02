import React from "react";
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav>
            <ul>
                <li><Link to ="/">Home</Link></li>
                <li><Link to ="/players">Players</Link></li>
                <li><Link to ="/quests">Quests</Link></li>
                <li><Link to ="/create-player">Create New Player</Link></li>
                <li><Link to ="/create-quest">Add Quest</Link></li>
            </ul>
        </nav>
    );
}

export default Navbar;