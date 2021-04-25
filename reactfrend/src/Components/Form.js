import React from 'react'
import {useState, useEffect} from 'react'
import Result from './Result'
import GMap from './GMap';
import data from '../data.json'

function UserForm({results}) {
    // const [eventData, setEventData] = useState([])
    // const [loading, setLoading] = useState(false)

    // useEffect(() => {
    //     const fetchEvents = async () =>{
    //         setLoading(true)
    //         const res = await fetch(' http://127.0.0.1:8080/data.json')
    //         const {locName} = await res.json()

    //         setEventData(locName)
    //         setLoading(false)
    //     }

    //     fetchEvents()
    //     console.log(eventData)
    // },[])
    
    return (
        <>
            <div class="container-fluid " >
            <br></br>
                    <br></br>
           
                    <input type="text" class="w-50 mx-auto text-center form-control" placeholder="Search Here" id="search" />
                    <br></br>
                <p class="m-3">Results: {results.length}</p>
                    
          
            <br></br><br></br>
            <GMap eventData={data}/>
            <br></br><br></br>
            <div class="row " >
            {results.map( result => {
                        return (
                            <Result result={result}/>
                        )
                    })}
            </div>
            </div>
        </>
    )
}

export default UserForm;