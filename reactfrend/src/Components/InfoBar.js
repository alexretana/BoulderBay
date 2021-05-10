import React from 'react'

export default function InfoBar({gym_data}) {

    // Set default values
    let link= '', gym_name= '', rating= '', address = '',address_geo
    
    // Try to assign values from gym_data
    try{
        link = "http://"+gym_data.gym_info[0]
        gym_name = gym_data.googleInfo.correct_name
        rating = "⭐ ".repeat(gym_data.googleInfo.rating)
        address = gym_data.gym_info[1].toUpperCase()
     
        address_geo = `http://maps.google.com//?ll=${gym_data.googleInfo.geoLoc[0]},${gym_data.googleInfo.geoLoc[1]}`
    }catch{

    }

    return (
        <>
        <div class="card info-bar" >
        <div class="card-body">
        <   a target="_blank"  href={link}><h3 class="card-title title">{gym_name}</h3></a>
            <p class="card-text">{rating}</p>
            <a target="_blank" href={address_geo}><p class="card-text"><h6>{address}</h6></p></a>
        
        </div>
        </div>

        </>
    )
}
