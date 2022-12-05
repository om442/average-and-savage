import React from 'react';
import "./carousel.css";
import trojan from './trojan.png';

function About() {
    return (
        <><div id="myCarousel" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <svg class="bd-placeholder-img" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false">
                        <rect width="100%" height="100%" fill="#212529" />
                        <image href={trojan} height="50%" width="100%" y="30px"/>
                    </svg>

                    <div class="container">
                        <div class="carousel-caption text-start">
                            <h1>Introducing The Team</h1>
                            <p>We are a group of motivated USC students working towards completing our graduate degrees. </p>
                        </div>
                    </div>
                </div>
            </div>
        </div><div class="container marketing">
                <div class="row text-center">
                    <div class="col-lg-3">
                        <h2 class="fw-normal">Parth Kapadia</h2>
                        <p>Parth bio.</p>
                    </div>
                    <div class="col-lg-3">
                        <h2 class="fw-normal">Sanjana Parakh</h2>
                        <p>Sanjana bio.</p>
                    </div>
                    <div class="col-lg-3">
                        <h2 class="fw-normal">Oscar Mui</h2>
                        <p>Oscar bio.</p>
                    </div>
                    <div class="col-lg-3">
                    <h2 class="fw-normal">Amit Birajdar</h2>
                    <p>Amit bio.</p>
                    </div>
                </div>
            </div></>
    );
}

export default About;