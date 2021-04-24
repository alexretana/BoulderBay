import React from 'react'
import {useState, useEffect} from 'react'
import Result from './Result'
import GMap from './GMap';

function UserForm({results}) {
    const [eventData, setEventData] = useState([])
    const [loading, setLoading] = useState(false)

    useEffect(() => {
        const fetchEvents = async () =>{
            setLoading(true)
            const res = await fetch('https://cors-anywhere.herokuapp.com/{ http://127.0.0.1:8080/data.json}')
            const {locName} = await res.json()

            setEventData(locName)
            setLoading(false)
        }

        fetchEvents()
        console.log(eventData)
    },[])

    return (
        <>
            <div class="container-fluid " >
                <br></br>
            <form class="form-inline  mx-auto" action="/action_page.php">
                <div class="form-group border border-warning">
                    <label for="email">Email: </label>
                    <input type="Email" class="ml-3 form-control" placeholder="Enter email" id="email" />
                </div>
                <div class="form-group m-3">
                    <label for="pwd">City: </label>
                    <input type="text" class="ml-3 form-control" placeholder="Enter password" id="pwd" />
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
                <p class="m-3">Results: {results.length}</p>
                    
            </form>
            <br></br><br></br>
            <GMap />
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