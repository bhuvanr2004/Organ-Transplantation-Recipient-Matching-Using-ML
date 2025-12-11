function viewLocation(latitude, longitude, name) {
    if (!latitude || !longitude) {
        alert('Location not available for this person.');
        return;
    }

    const googleMapsUrl = `https://www.google.com/maps?q=${latitude},${longitude}`;
    window.open(googleMapsUrl, '_blank');
}

function showLocationModal(latitude, longitude, name) {
    if (!latitude || !longitude) {
        alert('Location not available for this person.');
        return;
    }

    const modal = document.createElement('div');
    modal.className = 'modal fade show';
    modal.style.display = 'block';
    modal.style.backgroundColor = 'rgba(0,0,0,0.5)';
    modal.innerHTML = `
        <div class="modal-dialog modal-lg modal-dialog-centered">
            <div class="modal-content" style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-radius: 15px; border: 1px solid rgba(255, 255, 255, 0.2);">
                <div class="modal-header" style="border-bottom: 1px solid rgba(102, 126, 234, 0.1);">
                    <h5 class="modal-title">
                        <i class="fas fa-map-marked-alt"></i> Location: ${name}
                    </h5>
                    <button type="button" class="btn-close" onclick="this.closest('.modal').remove()"></button>
                </div>
                <div class="modal-body" style="padding: 0;">
                    <iframe 
                        width="100%" 
                        height="450" 
                        frameborder="0" 
                        style="border:0; border-radius: 0 0 15px 15px;" 
                        src="https://www.openstreetmap.org/export/embed.html?bbox=${longitude-0.01},${latitude-0.01},${longitude+0.01},${latitude+0.01}&layer=mapnik&marker=${latitude},${longitude}" 
                        allowfullscreen>
                    </iframe>
                </div>
                <div class="modal-footer" style="border-top: 1px solid rgba(102, 126, 234, 0.1);">
                    <div class="text-start flex-grow-1">
                        <small class="text-muted">
                            <i class="fas fa-map-pin"></i> 
                            Coordinates: <strong>${latitude.toFixed(6)}, ${longitude.toFixed(6)}</strong>
                        </small>
                    </div>
                    <a href="https://www.google.com/maps?q=${latitude},${longitude}" target="_blank" class="btn btn-sm btn-gradient">
                        <i class="fas fa-external-link-alt"></i> Open in Google Maps
                    </a>
                    <button type="button" class="btn btn-sm btn-outline-gradient" onclick="this.closest('.modal').remove()">
                        Close
                    </button>
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
}

function shareLocation(type, id) {
    if (!navigator.geolocation) {
        alert('Geolocation is not supported by your browser');
        return;
    }

    const button = document.getElementById(`location-btn-${type}-${id}`);
    if (button) {
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Getting location...';
        button.disabled = true;
    }

    navigator.geolocation.getCurrentPosition(
        function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            const endpoint = type === 'donor' 
                ? `/api/update_donor_location/${id}` 
                : `/api/update_recipient_location/${id}`;

            fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    latitude: latitude,
                    longitude: longitude
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert('Error: ' + data.error);
                } else {
                    alert('Location updated successfully!\nLatitude: ' + data.latitude.toFixed(6) + '\nLongitude: ' + data.longitude.toFixed(6));
                    location.reload();
                }
            })
            .catch(error => {
                alert('Error updating location: ' + error);
            })
            .finally(() => {
                if (button) {
                    button.innerHTML = '<i class="fas fa-map-marker-alt"></i> Share Location';
                    button.disabled = false;
                }
            });
        },
        function(error) {
            let errorMsg = 'Unable to get your location';
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    errorMsg = 'Location permission denied. Please enable location access in your browser settings.';
                    break;
                case error.POSITION_UNAVAILABLE:
                    errorMsg = 'Location information is unavailable.';
                    break;
                case error.TIMEOUT:
                    errorMsg = 'The request to get your location timed out.';
                    break;
            }
            alert(errorMsg);
            
            if (button) {
                button.innerHTML = '<i class="fas fa-map-marker-alt"></i> Share Location';
                button.disabled = false;
            }
        },
        {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 0
        }
    );
}
