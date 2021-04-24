import React from 'react'
import { useState } from 'react'
import GoogleMapReact from 'google-map-react'
import GymMarker from './gymMarker'

// define constants

const GMap = ({ eventData, center, zoom }) => {
    
    // console.log(Object.keys(eventData))
    const mapBoxStyle = {
        width : "50%",
        height: "80vh",
        margin: "auto",
    }
    
    const loopLocs = () =>{
        console.log(Object.entries(eventData))
    }
    return (
        <div style={ mapBoxStyle } className="map">
            <GoogleMapReact
                bootstrapURLKeys={{ key: 'AIzaSyAhv0uH1F1KkSjDVJwFzGBagH9tEFSDbcs' }}
                defaultCenter={ center }
                defaultZoom={ zoom }
            >
                <GymMarker lat ={42.3265} lng={-122.8756}/>
                <GymMarker lat ={43.3265} lng={-122.8756}/>
            
               { loopLocs()}
            </GoogleMapReact>
            {/* {locationInfo && <LocationInfoBox info={locationInfo} />} */}
        </div>
    )
}

GMap.defaultProps = {
    center: {
        lat: 42.3265,
        lng: -122.8756
    },
    zoom: 6
}

export default GMap