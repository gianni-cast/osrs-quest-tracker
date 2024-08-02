import React, { useEffect, useState } from "react";

function Quests() {
    const [quests, setQuests] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5555/quests')
            .then(resp => resp.json())
            .then(data => setQuests(data))
    }, [])

    return (<div>
        <h1>Available Quest</h1>
        <ol>
            {quests.map(quest => (
                <li key={quest.id}>{quest.name} (Description: {quest.description})</li>
            ))}
        </ol>
        </div>
    );
}

export default Quests;