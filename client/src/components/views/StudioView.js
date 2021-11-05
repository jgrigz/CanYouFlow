import React, { Fragment, useState, useEffect } from "react";
import { Link } from "react-router-dom";

export const StudioView = () => {
  const CREATE_GAME_URL = "http://localhost:8000/cyf-start-game/";
  const ALL_GAMES_URL = "http://localhost:8000/cyf-all-games/";

  const [games, setGames] = useState([{}]);
  const [form, setForm] = useState([{}]);

  const HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json",
  };

  useEffect(() => {
    // fetch(CREATE_GAME_URL, {
    //   HEADERS,
    // })
    //   .then((res) => res.json())
    //   .then((data) => setForm(data));

    fetch(ALL_GAMES_URL, {
      HEADERS,
    })
      .then((res) => res.json())
      .then((data) => setGames(data));
  }, []);

  console.log(games);

  return (
    <Fragment>
      <h2>Studio</h2>


      {games.map((game) => (
        <div
          className="card text-white bg-info mb-3"
          style={{ "max-width": "18rem;" }}
        >
          <div className="card-header">{game.player}</div>
          <div className="card-body">
            <h5 className="card-title">Started at: {game.created_at}</h5>
            <h6 className="card-title">Awards: {game.points_earned} points</h6>
            <h6 className="card-title">Beat: Drop drop it low</h6>
            <h6 className="card-title">Duration: 3 minutes</h6>
          </div>
        </div>
      ))}
    </Fragment>
  );
};
