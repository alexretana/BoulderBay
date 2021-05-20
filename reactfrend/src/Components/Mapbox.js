import React, { useRef, useEffect, useState } from 'react';
import './Styles/mapbox.css'
import 'mapbox-gl/dist/mapbox-gl.css';
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax

mapboxgl.accessToken =
  'pk.eyJ1IjoiZGJvaS1jdXJyeSIsImEiOiJja29kbm54MDYwMXhpMm9qeGw2aHN6aWpkIn0.wlCNtWwP70rQtX6J8vsX0w';

const Map = ({ eventData,geoLoc }) => {
  const mapContainerRef = useRef(null);
  const [lng, setLng] = useState(-97.65);
  const [lat, setLat] = useState(40.84);
  const [zoom, setZoom] = useState(3);
  const [center, setCenter] = useState(setLat,setLng);
  
  const setMarkers = (map) => {
    Object.keys(eventData).map(key => {
      try {
        // Getting gym geo location and rounding value
        // console.log(eventData[key].googleInfo.geoLoc)
        const getLat = Math.round(eventData[key].googleInfo.geoLoc[0])
        const getLng = Math.round(eventData[key].googleInfo.geoLoc[1])
        // Geting name to display
        const name = eventData[key].googleInfo.correct_name.substr(0,16)+"..."

        // console.log(eventData[key].gym_info[0])
        const gym_site = eventData[key].gym_info[0]
        if (getLng <= 90 && getLng <= 90) {

          // create a DOM element for the marker
          var el = document.createElement('div');
          el.className = 'marker';
          el.innerHTML = `<a target="_blank"  href="http://${gym_site}"><h5 class="markerText">${name}<img style="visibility:visible;width:50px;height:50px"src="https://www.flaticon.com/premium-icon/icons/svg/4357/4357659.svg"><h5><a>`
          
          // create map marker 
          new mapboxgl.Marker(el,
            { color: "black",
            }).setLngLat({ lat: getLat, lng: getLng }).addTo(map)
        } else {
          console.log("something went wrong creating marker div")
        }
      } catch { }
    })}

  // Initialize map when component mounts
  useEffect(() => {
    
    const map = new mapboxgl.Map({
      container: mapContainerRef.current,
      style: 'mapbox://styles/mapbox/outdoors-v11',
      center: geoLoc,
      zoom: zoom,
    });
    
    // Set up Markers and zoom
    setZoom(6)
    setMarkers(map)

    // Add navigation control (the +/- zoom buttons)
    map.addControl(new mapboxgl.NavigationControl(), 'top-right');

    map.on('move', () => {
      setLng(map.getCenter().lng.toFixed(4));
      setLat(map.getCenter().lat.toFixed(4));
      setZoom(map.getZoom().toFixed(2));
    });

    // Clean up on unmount
    return () => map.remove();
  }, [eventData]); // when user searches eventData updates and useEffect refreshes page

  return (
    <div>
      <div className="sidebarStyle">
      </div>
      <div style={{ "position":"relative","text-align":"right","color":"white","padding":"5px"}}>
        Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}
      </div>
      <div  className="map-container" ref={mapContainerRef} />
    </div>
  );
};

export default Map;