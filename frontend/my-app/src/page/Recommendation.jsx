import React, {useState, useEffect } from 'react';
import { Checkbox } from './Checkbox.jsx'; 
import axios from 'axios';


function Recommendation() {

    const [RecomendationRows, setRecomendationRows] = useState([])
    const [name,setName] = useState("")
    const [age,setAge] = useState("")
    const [gender,setGender] = useState("")
    const [linkedinURL,setLinkedinURL] = useState("")
    const [experience,setExperience] = useState("")

    const [likings, setLikings] = useState("") 
    const [preferences, setPreferences] = useState( { 'Python': false, 'Data Modelling': false, 'Statistical Analysis': false, 'Machine Learning' : false, 'Deep Learning' :  false} ) 

    function togglePreference(skill) { 
        preferences[skill] = !preferences[skill]; 
        let newLikings = ""; 
        for ( var skill in preferences ) { 
          if ( preferences[skill] ) { 
            newLikings += skill + ", "; 
          } 
        } 
        setLikings(newLikings); 
      } 

    function createRecomendationRows(data){
        let rows = []
        for (const [key,value] of Object.entries(data)){
            // if (value.trim() !== "")
                for (const [key,v] of Object.entries(value)){
                rows.push(<li class="list-group-item">{`${key}`} : {`${v}`}</li>)
                }
                rows.push(<li class="list-group-item"><br></br></li>)

        }

        
        setRecomendationRows(rows)
    }

    function formSubmitted(event){
        event.preventDefault()
        var name1 = name.replace(" ",'%20')
        var li = likings.trim()
        var skills = li.replace(" ",'%20')
        console.log(name1, linkedinURL,experience,skills,age,gender)
        console.log("URL Called: ", 'http://127.0.0.1:5000/recommendation?name='+name1+'&id='+linkedinURL+'&skills='+skills+'&experience='+experience+'&age='+age+'&gender='+gender)
        
        axios.get('http://127.0.0.1:5000/recommendation?name='+name1+'&id='+linkedinURL+'&skills='+skills+'&experience='+experience+'&age='+age+'&gender='+gender)
        
        .then(res => {
            // const persons = res.data;
            // this.setState({ persons });
            createRecomendationRows(res.data)
          })    
        }

    return (
        <>
        <div class="alert alert-primary text-center" role="alert">
        Need help? Follow the below steps to get a curated set of recommended partners!
        </div>
        <div class="container text-center">
            <div class="row">
                <div class="col">
                    <div class="card text-bg-secondary mb-3">
                            <div class="card-header">Step 1</div>
                            <div class="card-body">
                                <p class="card-text">Use the button below to import your LinkedIn profile data using the LinkedIn API.</p>
                            </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card text-bg-secondary mb-3">
                            <div class="card-header">Step 2</div>
                            <div class="card-body">
                                <p class="card-text">Choose filters that best fit your needs. These parameters will be removed from the results.</p>
                            </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card text-bg-secondary mb-3">
                            <div class="card-header">Step 3</div>
                            <div class="card-body">
                                <p class="card-text">And... voila! You're done! The results are the best matched individuals from our dataset.</p>
                            </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container">
            <div class="row">
                <div class="input-group mb-3">
                    <button type="button" class="btn btn-secondary" style={{width: "100%", height: "43px", backgroundColor: "#007bff", marginLeft: "0px"}}>Import your LinkedIn Profile here...</button>
                </div>
            </div>


        <form onSubmit={(event) => formSubmitted(event)}>
            <div class="grid-container-element">
                <div class="grid-child-element purple">
                    <label>Name</label>
                    <input type="text" onChange={(event) => setName(event.target.value)} />
                </div>
                <div class="grid-child-element green">
                    <label>Email ID</label>
                    <input type="text" onChange={(event) => setLinkedinURL(event.target.value)} /> 
                </div>
            </div>
            <br></br>

            {/* <div class="center"><label >FILTERS</label></div> */}
            <div class="container">
            <div class="row">
                <div class="input-group mb-3">
                    <button type="button" class="btn btn-secondary" style={{width: "110%", height: "43px", backgroundColor: "#a6b0ba", marginLeft: "0px", color : 'black'}}>FILTERS</button>
                </div>
            </div>
            </div>

            <div class="grid-container-element">
                
                <div class="grid-child-element green">
                <label>Minimum Experience</label>
                <input type="text" onChange={(event) => setExperience(event.target.value)} /> 
                </div>

                <div class="grid-child-element green">
                <label>Age</label>
                <input type="text" onChange={(event) => setAge(event.target.value)} /> 
                </div>

                <div class="grid-child-element green">
                <label>Gender</label>
                <input type="text" onChange={(event) => setGender(event.target.value)} /> 
                </div>

                <div class="grid-child-element green">
                <label>Skills</label>

                <div> 
    
                <Checkbox onText="Python" offText="Python" togglePreference={togglePreference} skill="Python" /> 
                <Checkbox onText="Data Modelling" offText="Data Modelling" togglePreference={togglePreference} skill="Data Modelling" /> 
                <Checkbox onText="Statistical Analysis" offText="Statistical Analysis" togglePreference={togglePreference} skill="Statistical Analysis" /> 
                <Checkbox onText="Deep Learning" offText="Deep Learning" togglePreference={togglePreference} skill="Deep Learning" />
                <Checkbox onText="Machine Learning" offText="Machine Learning" togglePreference={togglePreference} skill="Machine Learning" />

                </div> 

                </div>

            </div>
            
            <div class="center">
                <input type="submit" style={{width: "50%", height: "30px"}}/>
                {/* <button onClick={() => setSearch(!search)}>submit</button> */}
            </div>
        </form>


        </div>

        <div class="container">
            <div class="row">
                <ul class="list-group">
                    {RecomendationRows}
                </ul>
            </div>
        </div>

        <br></br>
        <br></br>
        </>
        );
    }

export default Recommendation;