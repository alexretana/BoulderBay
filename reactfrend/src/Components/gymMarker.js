
export default function GymMarker({ lat, lng, onHover   }) {
    const marker = {
        color:"red"
    }
    return (
        <div className="gym-marker" onHover={onHover}>
            <h1>title</h1>
            <svg style={marker} xmlns="http://www.w3.org/2000/svg" width="50" height="60" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
  <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/>
</svg>
        </div>
    )
}
