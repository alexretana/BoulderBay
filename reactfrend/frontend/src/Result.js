import React from 'react'

export default function Result({ result }) {
    return (
        <div>
            <div class="container-fluid">
              <div class="row">
              <div class="col-sm-12 col-md-6 col-lg-4">
               <div class="card">
                    <div class="card-body">Basic card</div>
                    <p>{result.title}</p>
                    <p>{result.rating}</p>
                    <p>{result.address}</p>
                </div>
               </div>
              </div>
            </div>

        </div>
    )
}
