import React, {useState} from 'react'; 

function Checkbox(props) { 
  
  const [checked, setChecked] = useState(false); 
  const checkedText = props.onText; 
  const uncheckedText = props.offText; 
  const togglePreference = props.togglePreference; 
  const skill = props.skill; 
  const handleChange = () => { 
    
    setChecked(!checked); 
    togglePreference(skill); 
    
  }; 
  return ( 
    <div> 
      <p>
        <input type="checkBox" onChange={handleChange} style={{paddingRight: "2px"}}></input>
        {checked ? skill : skill}
      </p> 
      
    </div> 
  ); 
  
}
export {Checkbox};