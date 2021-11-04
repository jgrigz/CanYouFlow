import React, { Fragment, useEffect } from "react";
import { Link } from "react-router-dom";

export const NavigationBar = () => {
  return (
    <Fragment>
      <div>
        <nav class="navbar navbar-dark bg-dark">
          <div class="container-fluid">
            <Link to ='/home/' class="navbar-brand" >
              🎤CanYouFlow?
            </Link>
            <button
              class="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                  <Link to="/home/" style={{ marginRight: "12px", color: "gold" }} class="nav-link active" aria-current="page" href="#">
                    Home
                  </Link>
                </li>
                <li class="nav-item dropdown">
                  <Link
                    to="#"
                    style={{ marginRight: "12px", color: "gold" }}
                    class="nav-link dropdown-toggle"
                    href="#"
                    id="navbarDropdown"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Social
                  </Link>
                  <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li>
                      <a class="dropdown-item" href="/all_users/">
                        Artists
                      </a>
                    </li>
                    <li>
                      <Link
                        to="#"
                        class="dropdown-item"
                        href="#"
                      >
                        Messages
                      </Link>
                    </li>
                    <li>
                      <Link
                        to="/dashboard"
                        class="dropdown-item"
                        href="#"
                      >
                        Video Call
                      </Link>
                    </li>
                  </ul>
                </li>
                <li class="nav-item dropdown">
                  <Link
                    to="/dashboard"
                    style={{ marginRight: "12px", color: "gold" }}
                    class="nav-link dropdown-toggle"
                    href="#"
                    id="navbarDropdown"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Studio
                  </Link>
                  <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li>
                      <Link
                        to="#"
                        class="dropdown-item"
                        href="#"
                      >
                        Songs
                      </Link>
                    </li>
                    <li>
                      <Link
                        to="#"
                        class="dropdown-item"
                        href="#"
                      >
                        Add Song
                      </Link>
                    </li>
                  </ul>
                </li>
              </ul>
              <form class="d-flex">
                <input
                  class="form-control me-2"
                  type="search"
                  placeholder="Search A Rhyme"
                  aria-label="Search"
                />
                <button class="btn btn-outline-success" type="submit">
                  Search
                </button>
              </form>
            </div>
          </div>
        </nav>
      </div>
    </Fragment>
  );
};
