
import React from 'react'
import Result from './Result'
import Mapbox from './Mapbox';
function UserForm({results}) {
    return (
        <>
            <div class="container-fluid " >
                <br></br>
            <form class="form-inline  mx-auto" action="/action_page.php">
                <div class="form-group border border-warning">
                    <label for="email">Email: </label>
                    <input type="Email" class="ml-3 form-control" placeholder="Enter email" id="email" />
                </div>
                <div class="form-group m-3">
                    <label for="pwd">City: </label>
                    <input type="text" class="ml-3 form-control" placeholder="Enter password" id="pwd" />
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
                <p class="m-3">Results: {results.length}</p>
                    
            </form>
            <br></br><br></br>
            <Mapbox />
            <br></br><br></br>
            <div class="row " >
            {results.map( result => {
                        return (
                            <Result result={result}/>
                        )
                    })}
            </div>
            </div>
        </>
    )
}

export default UserForm;