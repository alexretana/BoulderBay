import React from 'react'

export default function ReactMap() {
    var mapboxgl = require('mapbox-gl/dist/mapbox-gl.js');

    mapboxgl.accessToken = 'pk.eyJ1IjoiZGJvaS1jdXJyeSIsImEiOiJja250Mmk2NDEwMHgyMm9vYzU3OWU5a2NyIn0.1M7uVyFPUuLaU9PlVNVT2A';
    var map = new mapboxgl.Map({
      container: 'YOUR_CONTAINER_ELEMENT_ID',
      style: 'mapbox://styles/mapbox/streets-v11'
    });
    
    return (
        <div>
            {mapboxgl}
        </div>
    )
}
