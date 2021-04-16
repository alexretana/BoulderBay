import React from 'react'

export default function Result({ result }) {
    return (
        <div>
            <div class="container">
              
              <div class="col-sm-12 ">
               <div class="card ">
                    <div class="card-body ">
                    <p>{result.title}</p>
                    <p>{result.rating}</p>
                    <p>{result.address}</p>
                    </div>
                    
                </div>
               </div>
              
            </div>
            <br></br>
        </div>
    )
}
