import React from 'react';
import {useState} from 'react'; 
import {Link } from "react-router-dom";

function Home() {
    return (

        <div class="container-fluid text-center text-bg-dark vh-100">
            <div style={{height: "100px"}}></div>
            <h1>Find your next partner.</h1>
            <div style={{marginLeft: "300px", marginRight: "300px"}}>
                    <p class="lead">Our recommendation system is a one-stop shop for finding relatable and compatible partners to collaborate on data science projects.</p>
                    <p class="lead">Simply upload your LinkedIn profile, choose your filters, and we'll do the rest!</p>
            </div>
            <div style={{height: "50px"}}></div>
            <h2>Ready to get started?</h2><br></br>
            <Link to="/Recommendation">
                <button type="button" class="btn btn-light" style={{width: "150px", height: "60px", fontWeight: "bold", backgroundColor: "#008CBA", fontSize: "24px"}}>Let's Go!</button>
            </Link>
        </div>
    );
}

export default Home;