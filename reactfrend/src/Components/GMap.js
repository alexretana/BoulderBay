import React from 'react'
import { useState, useEffect } from 'react'
import GoogleMapReact from 'google-map-react'
import GymMarker from './gymMarker'

// define constants

const GMap = ({eventData}) => {
    
    let center = {lat: 38.54555438314078,
        lng: -97.9853579502318}
    const zoom = 8
    const mapBoxStyle = {
        width: "100%",
        height: "100vh",
    }
    
    // find avg lat and lng to center search
    const avg_loc = (data) => {
        let avg_GeoLoc = {}
        Object.keys(data).map( key =>{
            // console.log(data[key]['googleInfo']['geoLoc'])
            Object.assign(avg_GeoLoc,data[key]['googleInfo']['geoLoc'])
        })
        console.log(avg_GeoLoc)
        return avg_GeoLoc
    }
    // center = avg_loc(eventData)
    
    // create array and to add name, rating and geoLoc
    const locMarkers = []
    const Markers = () => {
        for (const i in Object.keys(eventData)) {
            // console.log(eventData[Object.keys(eventData)[i]])
            const gInfo = eventData[Object.keys(eventData)[i]]['googleInfo']

            const lat = gInfo['geoLoc'][0]
            const lng = gInfo['geoLoc'][1]
            const name = gInfo['correct_name']
            const rating = gInfo['rating']

            if (typeof (lat) === "number") {
                locMarkers.push(
                    {
                        name: name,
                        rating: rating,
                        geoLoc: [lat, lng]
                    }
                )
            }
        }
    }
    Markers()



    return (
        <div style={mapBoxStyle} className="map">
            <GoogleMapReact
                bootstrapURLKeys={{ key: 'AIzaSyDtggfQvcGa_TB9YlG3vWRMKAe2Q4orUr8' }}
                defaultCenter={center}
                defaultZoom={zoom}
            >

                {locMarkers.map(ev => {
                    // console.log(ev[0],ev[1])
                    return <GymMarker ginfo={ev} lat={ev['geoLoc'][0]} lng={ev['geoLoc'][1]} />
                })}

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
    zoom: 5
}

export default GMap