import React from 'react'
import { useState, useEffect } from 'react'
import GoogleMapReact from 'google-map-react'
import GymMarker from './gymMarker'

// define constants

const GMap = ({ eventData, center, zoom }) => {
    // console.log(Object.keys(eventData))
    const locMarkers = []
    const mapBoxStyle = {
        width : "50%",
        height: "80vh",
        margin: "auto",
    }
    
    
       
    const Markers = () =>{
        for (const i in Object.keys(eventData)){
            // console.log(eventData[Object.keys(eventData)[i]]['geoloc'])

            const lat = eventData[Object.keys(eventData)[i]]['gInfo']['geoLoc'][0]
            const lng = eventData[Object.keys(eventData)[i]]['gInfo']['geoLoc'][1]

            locMarkers.push([lat,lng])
        }
    }
    Markers()

    const output = locMarkers.map(ev =>{
        console.log(ev[0],ev[1])
        return <GymMarker lat ={ev[0]} lng={ev[1]}/>
    })
   
    return (
        <div style={ mapBoxStyle } className="map">
            <GoogleMapReact
                bootstrapURLKeys={{ key: 'AIzaSyAhv0uH1F1KkSjDVJwFzGBagH9tEFSDbcs' }}
                defaultCenter={ center }
                defaultZoom={ zoom }
            >
               
            {output}
               
            </GoogleMapReact>
            {/* {locationInfo && <LocationInfoBox info={locationInfo} />} */}
        </div>
    )
}

GMap.defaultProps = {
    center: {
        lat: 38.54555438314078,
        lng: -97.9853579502318
    },
    zoom: 4
}

export default GMap