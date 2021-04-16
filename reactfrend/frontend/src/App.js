import React, {useState} from 'react'
import UserForm from './Form'


function App() {
  const [results, setresults] = useState([
    
    {
      title:"result1",
      rating:"⭐⭐⭐⭐",
      address:"5270 N US HWY 1, Palm Shores, FL 32940 "
    },
    {
      title:"result2",
      rating:"⭐⭐⭐⭐",
      address:"5270 N US HWY 1, Palm Shores, FL 32940 "
    },
    {
      title:"result1",
      rating:"⭐⭐⭐⭐",
      address:"5270 N US HWY 1, Palm Shores, FL 32940 "
    },
    {
      title:"result2",
      rating:"⭐⭐⭐⭐",
      address:"5270 N US HWY 1, Palm Shores, FL 32940 "
    }
  
  ])
  return (
        <UserForm results={results}/>
      );
}

export default App;
