import React from 'react';

function Projects() {
    return (
        <div style={{marginLeft: "70px", marginRight: "70px"}}>
            <div class="alert alert-dark" role="alert">
                <strong>Not sure where to go next? </strong>
                Check out the resources below for some inspiration!
            </div>
            <div class="alert alert-info" role="alert">
                <h1>Kaggle</h1>
                Kaggle is an online community platform for data scientists and machine learning enthusiasts. Kaggle allows users to collaborate with other users, find and publish datasets, use GPU integrated notebooks, and compete with other data scientists to solve data science challenges. This is one of the most popular destinations for data science competitions.
                <br></br><br></br>
                You can check it out <a href="https://www.kaggle.com/" class="alert-link">here</a>.
            </div>
            <div class="alert alert-info" role="alert">
                <h1>Data Driven</h1>
                DataDriven aims create social impact by tackling pressing challenges using data science hence many competitions are related to health, climate change, education and conservation. Similar to Kaggle, the context, problem description, evaluation metrics and data are clearly explained.
                <br></br><br></br>
                You can check it out <a href="https://www.drivendata.org/competitions/" class="alert-link">here</a>.
            </div>
            <div class="alert alert-info" role="alert">
                <h1>RMDS</h1>
                Interest in blockchain? The RMDS has been building and serving data and research communities since 2009. With a global community of more than 40,000 members, the RMDS Lab was created in 2019 to serve its members and partners, and to be owned by its members and partners worldwide. RMDS Lab created the world’s first NFT marketplace for science IPs, in combination with its RMDS Ecosystem to solve the four big problems all scientists face: funding difficulties, high project failure ratios, low IP utilization, and the replication crisis.
                <br></br><br></br>
                You can check it out <a href="https://www.rmdslab.com/" class="alert-link">here</a>.
            </div>
            <div class="alert alert-info" role="alert">
                <h1>Codalab</h1>
                Codalab is an open-source web-based platform that enables researchers, developers, and data scientists to collaborate to advance research fields where machine learning and advanced computation are used. CodaLab helps solve many common problems in data-oriented research through its online community, where people can share worksheets and participate in competitions.
                <br></br><br></br>
                You can check it out <a href="https://codalab.org/" class="alert-link">here</a>.
            </div>
        </div>
    );
}

export default Projects;