import React from "react";
import { BrowserRouter, Route, Link } from "react-router-dom";

function Navbar() {
  return (
    <nav class="navbar background" style={{height: "80px"}}>
      <ul class="nav-list">
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/Recommendation">Recommendation</Link>
        </li>
        <li>
          <Link to="/Projects">Projects</Link>
        </li>
        <li>
          <Link to="/About">About</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;