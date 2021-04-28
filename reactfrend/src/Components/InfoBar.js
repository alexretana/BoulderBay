import React from 'react'

export default function InfoBar({gym_data}) {
    // console.log(gym_data)
    return (
        <>
        <div class="card" >
        <div class="card-body">
            <h3 class="card-title">{gym_data.googleInfo.correct_name}</h3>
            <p class="card-text">{"⭐ ".repeat(gym_data.googleInfo.rating)}</p>
            <p class="card-text">Address: {gym_data.gym_info[1]}</p>

        </div>
        </div>

        </>
    )
}
