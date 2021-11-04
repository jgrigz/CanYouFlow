import React, { Fragment, useEffect } from "react";
import { Link } from "react-router-dom";

export const IndexView = () => {
  return (
    <Fragment>
      <div>
        <h2>Welcome!</h2>

        <h3>Dont Have an Account?</h3>
        <Link to="/register/">
          <button>Register</button>
        </Link>
        <h3>Already a Member?</h3>
        <Link to="/login/">
          <button>Login</button>
        </Link>
      </div>
    </Fragment>
  );
};
