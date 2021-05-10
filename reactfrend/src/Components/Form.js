import React from 'react'
import { useState, useEffect, useRef } from 'react'
import Mapbox from './Mapbox'
import Infobar from './InfoBar'
import data from '../data.json'
import './Styles/sidebar.css'

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

   
    // let avg_center = {
    //     lat: 38.54555438314078,
    //     lng: -97.9853579502318
    // }
    const search_results = {}
    const [search, setSearch] = useState('')
    const [filtered_data, setfiltered_data] = useState({})
    const [geoLoc, setGeoLoc] = useState([-90.9, 40])

    // When search value changes check for matches
    useEffect(() => {
        // return filtered out data Object to plug into map and infobox
        Object.keys(data).map(key => {
            // if state equals to search add to filtered data
            if (search.toLowerCase() == data[key]['state'].toLowerCase()) {
                search_results[key] = data[key]
                setfiltered_data(search_results)

                // set geo location
                if (Object.keys(search_results).length) {
                    console.log('search_results exist centering')
                    const geoLat = Math.round(search_results[Object.keys(search_results)[0]].googleInfo.geoLoc[0])
                    const geoLng = Math.round(search_results[Object.keys(search_results)[0]].googleInfo.geoLoc[1])

                    setGeoLoc([geoLng, geoLat])
                } else {
                    console.log('search_results does not exist')
                }
            }
            else {
                console.log('nothing to add')
            }
        })
    }, [search]) // useEffect looks at search for changes and updates as needed

    return (
        <>
            <div style={{background:"#3f4f78"}}class="container-fluid" >
                <div class="row" >
                    <div class="col-md-9 col-sm-12 " >
                    <input className="search" type="text" onChange={(e) => setSearch(e.target.value)} placeholder="Search"></input>
                        {/* <GMap eventData={filtered_data} geoLoc={geoLoc}/> */}
                        <Mapbox eventData={filtered_data} geoLoc={geoLoc} />
                    </div><br></br>
                    <div class="list-box col-md-3 col-sm-12" >
                        {
                            Object.keys(filtered_data).map(key => {
                                return (<Infobar gym_data={filtered_data[key]} />)
                            })
                        }
                    </div>
                </div>
            </div>
        </>

    )
}

export default UserForm;