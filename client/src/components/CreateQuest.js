import React, { useEffect, useState } from "react";
import { useFormik } from "formik";
import * as Yup from "yup";

const API = 'http://127.0.0.1:5555/quests';

const initialQuestInfo = {
    name: "",
    description: "",
}

const validationSchema = Yup.object({
    name: Yup.string().required("Quest name is required"),
    description: Yup.string().required("Description is required")
});

function CreateQuest() {
    const [quests, setQuests] = useState([]);
    const [refreshPage, setRefreshPage] = useState(false);

    useEffect(() => {
        fetch(API)
            .then(resp => resp.json())
            .then(data => setQuests(data))
    }, [refreshPage])

    const formik = useFormik({
        initialValues: initialQuestInfo,
        validationSchema: validationSchema,
        onSubmit: values => {
            addPlayer(values)
        }
    })

    function addPlayer(newQuest) {
        fetch(API, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newQuest)
        })
        .then((resp) => {
            if (resp.status == 200) {
                setRefreshPage(!refreshPage)
            }
        })
    }

    return (
        <div className="form-container">
            <h1>Add a New Quest</h1>
            <form onSubmit={formik.handleSubmit}>
                <div>
                    <input
                        type="text"
                        name="name"
                        placeholder="Enter Quest Name"
                        value={formik.values.name}
                        onChange={formik.handleChange}
                    />
                    <p style={{ color: "red" }}> {formik.errors.name}</p>
                </div>
                <div>
                    <input
                        type="text"
                        name="description"
                        placeholder="Enter Description"
                        value={formik.values.description}
                        onChange={formik.handleChange}
                    />
                    <p style={{ color: "red" }}> {formik.errors.description}</p>
                </div>
                <button type="submit">Add New Quest</button>
            </form>
            <h2>Current Quests</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {quests.length === 0 ? (
            <tr><td>No players available</td></tr>
          ) : (
            quests.map((quest) => (
              <tr key={quest.id}>
                <td>{quest.name}</td>
                <td>{quest.description}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
        </div>
    );
}

export default CreateQuest;