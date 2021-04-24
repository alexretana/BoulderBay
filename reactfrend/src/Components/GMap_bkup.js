import React from 'react'
import { GoogleMap, Marker, useJsApiLoader, withGoogleMap, withScriptjs, InfoWindow  } from '@react-google-maps/api';

const containerStyle = {
  width: '50%',
  height: '400px',
  margin: 'auto',
  "border-radius":"10px"
};

const center = {
  lat: -3.745,
  lng: -38.523
};

function MyComponent() {
  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: "AIzaSyAhv0uH1F1KkSjDVJwFzGBagH9tEFSDbcs"
  })

  const [map, setMap] = React.useState(null)

  const onLoad = React.useCallback(function callback(map) {
    const bounds = new window.google.maps.LatLngBounds();
    map.fitBounds(bounds);
    setMap(map)
  }, [])

  const onUnmount = React.useCallback(function callback(map) {
    setMap(null)
  }, [])

  return isLoaded ? (
      <GoogleMap
        mapContainerStyle={containerStyle}
        center={center}
        zoom={10}
        onLoad={onLoad}
        onUnmount={onUnmount}
      >
        { /* Child components, such as markers, info windows, etc. */ 
         <Marker
         position={"-3|-38.2"}
       />
        }
        
        <></>
      </GoogleMap>
  ) : <></>
}

export default React.memo(MyComponent)