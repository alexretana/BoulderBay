import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
 
const AnyReactComponent = ({ text }) => <div>{text}</div>;
 
class SimpleMap extends Component {
  static defaultProps = {
    center: {
      lat: 59.95,
      lng: 30.33
    },
    zoom: 11
  };
 
  render() {
    return (
      <>
      <div style={{ height: '100vh', width: '85%', margin:"auto" }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: "AIzaSyDtggfQvcGa_TB9YlG3vWRMKAe2Q4orUr8" }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
        >
          <AnyReactComponent
            lat={59.955413}
            lng={30.337844}
            text="My Marker"
          />
        </GoogleMapReact>
      </div>
      </>
    );
  }
}
 
export default SimpleMap;