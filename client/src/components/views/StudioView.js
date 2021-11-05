import React, { Fragment, useState, useEffect } from "react";
import { Link } from "react-router-dom";

export const StudioView = () => {
  const CREATE_GAME_URL = "http://localhost:8000/cyf-start-game/";
  const ALL_GAMES_URL = "http://localhost:8000/cyf-all-games/";

  const [game, setGame] = useState([{}]);
  const [form, setForm] = useState([{}]);

  const HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json",
  };

  useEffect(() => {
    fetch(CREATE_GAME_URL, {
      HEADERS,
    })
      .then((res) => res.json())
      .then((data) => setForm(data));
  }, []);

  console.log(form);

  return (
    <Fragment>
      <h2>Studio</h2>
    </Fragment>
  );
};
