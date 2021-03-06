import "./App.css";
import React, { Fragment, useState, useEffect } from "react";
import { render } from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { NavigationBar } from "./components/views/Navigation";
import { IndexView } from "./components/views/IndexView";
import { Login } from "./components/views/Login";
import { Register } from "./components/views/Register";
import { HomeView } from "./components/views/HomeView";
import { StudioView } from "./components/views/StudioView";
import { AllUsersView } from "./components/views/AllUsersView";

function App() {
  return (
    <Fragment>
      <BrowserRouter>
        <NavigationBar />
        <Routes>
          <Route path="/" element={<IndexView />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<HomeView />} />
          <Route path="/studio" element={<StudioView />} />
          <Route path="/all-users" element={<AllUsersView />} />
        </Routes>
      </BrowserRouter>
    </Fragment>
  );
}

export default App;
