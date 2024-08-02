import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Navbar from "./Navbar";
import Home from "./Home";
import Players from "./Players";
import Quests from "./Quests";
import PlayerDetails from "./PlayerDetails";
import CreatePlayer from "./CreatePlayer";
import CreateQuest from "./CreateQuest";

function App() {
  return (
    <>
      <Navbar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/players" component={Players} />
        <Route path="/quests" component={Quests} />
        <Route path="/players/:id" component={PlayerDetails} />
        <Route path="/create-player" component={CreatePlayer} />
        <Route path="/create-quest" component={CreateQuest} />
      </Switch>
    </>
  );
}

export default App;
