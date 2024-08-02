import React, { useEffect, useState } from "react";
import { useFormik } from "formik";
import * as Yup from "yup";

const API = 'http://127.0.0.1:5555/players';

const initialPlayerInfo = {
    name: "",
    level: "",
}

const validationSchema = Yup.object({
    name: Yup.string().required("Name is required"),
    level: Yup.number().min(3).max(126).required("Level must be between 3 and 126")
});

function CreatePlayer() {
    const [players, setPlayers] = useState([]);
    const [refreshPage, setRefreshPage] = useState(false);

    useEffect(() => {
        fetch(API)
            .then(resp => resp.json())
            .then(data => setPlayers(data))
    }, [refreshPage])

    const formik = useFormik({
        initialValues: initialPlayerInfo,
        validationSchema: validationSchema,
        onSubmit: values => {
            addPlayer(values)
        }
    })

    function addPlayer(newPlayer) {
        fetch(API, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newPlayer)
        })
        .then((resp) => {
            if (resp.status == 200) {
                setRefreshPage(!refreshPage)
            }
        })
    }

    return (
        <div className="form-container">
            <h1>Create a New Adventurer</h1>
            <form onSubmit={formik.handleSubmit}>
                <div>
                    <input
                        type="text"
                        name="name"
                        placeholder="Enter Name"
                        value={formik.values.name}
                        onChange={formik.handleChange}
                    />
                    <p style={{ color: "red" }}> {formik.errors.name}</p>
                </div>
                <div>
                    <input
                        type="number"
                        name="level"
                        placeholder="Enter Level"
                        value={formik.values.level}
                        onChange={formik.handleChange}
                    />
                    <p style={{ color: "red" }}> {formik.errors.level}</p>
                </div>
                <button type="submit">Create Player</button>
            </form>
            <h2>Current Players</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Level</th>
          </tr>
        </thead>
        <tbody>
          {players.length === 0 ? (
            <tr><td>No players available</td></tr>
          ) : (
            players.map((player) => (
              <tr key={player.id}>
                <td>{player.name}</td>
                <td>{player.level}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
        </div>
    );
}

export default CreatePlayer;