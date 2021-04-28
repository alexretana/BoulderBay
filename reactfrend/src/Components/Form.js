import React from 'react'
import { useState, useEffect, useRef } from 'react'
import Result from './Result'
import GMap from './GMap';
import Infobar from './InfoBar'
import data from '../data.json'

function UserForm() {
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

    const panel_style = {
        // position:"fixed",
        position: "relative",
        float: "left",
        "z-index": "3000",
        height: "100vh",
        overflow: "scroll",
        background: "rgba(29, 53, 87, 0.9)",
        "border-radius": 0,
        color: "white",
        padding: "25px"
    }
    let avg_center = {
        lat: 38.54555438314078,
        lng: -97.9853579502318
    }
    const search_results = {}
    const [search, setSearch] = useState('')
    const [filtered_data, setfiltered_data] = useState({})
    
      
    // When search value changes check for matches
    useEffect(() => {
        // return filtered out data Object to plug into map and infobox
        Object.keys(data).map(key => {
            // if state equals to search add to filtered data
            if (search == data[key]['state']) {
                search_results[key] = data[key]
            }
            else {
                console.log('nothing to add')
            }
        })
        setfiltered_data(search_results)
    }, [search])

    return (
        <>
            <div class="container-fluid" >
                <div class="row" >

                    <div class="col-sm-12 col-md-3 " style={panel_style}>
                        <input className="form-control" type="text" onChange={(e) => setSearch(e.target.value)}  placeholder="Search"></input>
                        {
                        
                            Object.keys(filtered_data).map(key => {
                                return (
                                    <Infobar gym_data={filtered_data[key]} />
                                )
                            })
                        
                        }
                    </div>
                    <div class="" >
                        <GMap eventData={filtered_data} center={avg_center}/>
                    </div>
                </div>
            </div>
        </>
    )
}

export default UserForm;