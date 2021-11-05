import React, { Fragment, useState, useEffect } from "react";
import { Link } from "react-router-dom";

export const AllUsersView = () => {
  const ALL_USERS_URL = "http://localhost:8000/cyf-all-users/";

  const [users, setUsers] = useState([{}]);

  const HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json",
  };

  useEffect(() => {
    fetch(ALL_USERS_URL, {
      HEADERS,
    })
      .then((res) => res.json())
      .then((data) => setUsers(data));
  }, []);

  console.log(users);

  return (
    <Fragment>
      <h2>Current Artists</h2>

      {users.map((user) => (
        <div
          className="card text-white bg-info mb-3"
          style={{ "max-width": "18rem;" }}
        >
          <div className="card-header">User: {user.username}</div>
          <div className="card-body">
            <h5 className="card-title">Name: {user.full_name}</h5>
            <h6 className="card-title">Email: {user.email}</h6>
            <h6 className="card-title">Joined on: {user.created_at}</h6>
          </div>
        </div>
      ))}
    </Fragment>
  );
};
