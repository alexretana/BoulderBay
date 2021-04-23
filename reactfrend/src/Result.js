import React from 'react'


export default function Result({ result }) {
    return (
        <>
            
            <div class="card col-sm-12 col-md-3 w-100 ">

                <div class="card w-100">
                    <img class="card-img-top" src="..." alt="Card image cap"></img>
                    <div class="card-body">
                        <h5 class="card-title">{result.title}</h5>
                        <p class="card-text">{result.rating}</p>
                        <p class="card-text">{result.address}</p>
                        <div id='map' style={{width: "400px",height: "300px"}}></div>
                       
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>

            </div>



        </>
    )
}