var map = null;
var coordinates = {};
var details = {};
// Initialize and add the map
function initMap() {
    // The map, centered at Dhaka
    map = new google.maps.Map(
        document.getElementById('map'), {zoom: 15, center: {lat: 23.7104, lng: 90.40744}});
}

updateMap = () => {
    centerCords = getCenterIndex();

    // The map, centered at the middle result
    map = new google.maps.Map(
        document.getElementById('map'), {zoom: 15, center: coordinates[centerCords]});
    addMarker(coordinates);
}

getCenterIndex = () => {
    centerIndex = parseInt(Object.keys(coordinates).length / 2);
    var i = 0;
    for (x in coordinates) {
        i++;
        if (i == centerIndex) {
            return x;
        }
    }
}

addMarker = (coordinates) => {
    for (let [key, cord] of Object.entries(coordinates)) {
        // Set the marker
        var marker = new google.maps.Marker({position: cord, map: map});

        //Listen for clicks on the map.
        google.maps.event.addListener(marker, 'click', function() { 
            getDetails(key); 
        }); 
    }
}

// Search all data by category
search = () => {
    var address = document.getElementById('address').value.trim();
    var category = document.getElementById('category').value;

    if (!address) {
        alert('Please enter an address!');
        return;
    }
    if (category === 'Choose...') {
        alert('Please select a category!');
        return;
    }
    var jqxhr = $.get( `query?address=${address}&category=${category}`, () => {})
        .done((data) => {
            coordinates = JSON.parse(data);
            if (Object.keys(coordinates).length > 0) {
                updateMap();
            }
            else {
                alert('No results found!');
                initMap();
            }
        })
        .fail((error) => {
            console.log( 'error' );
        });
}

// Get place details by place_id
getDetails = (place_id) => {
    if (!place_id) {
        alert('Invalid place id!');
        return;
    }

    var jqxhr = $.get( `details?place_id=${place_id}`, () => {})
        .done((data) => {
            details = JSON.parse(data);
            if (details.name) {
                renderDetails();
            }
            else {
                alert('Can\'t find the place!');
            }
        })
        .fail((error) => {
            console.log( 'error' );
        });
}

// Render details in the modal
renderDetails = () => {
    var modal = document.getElementById('modalContent');
    var reviewsStr = '<div class="row">';
    var reviews = details['reviews'];
    if (details['reviews'] && details['reviews'].length > 3 ) {
        reviews = reviews.slice(0, 3);
    }
    
    if (reviews) {
        reviews = reviews.map((review) => {
            reviewsStr += `<div class="col-sm-4">
                                <div class="card">
                                    <div class="card-body">
                                        <h6 class="card-title">${review.author_name || 'N/A'}</h6>
                                        <p class="card-text">Review: ${review.text || 'N/A'}</p>
                                        <p class="card-text">Rating: ${review.rating || 'N/A'}</p>
                                        <p class="card-text">Time: ${review.relative_time_description || 'N/A'}</p>
                                    </div>
                                </div>
                            </div>`
        });

        reviewsStr += '</div>';
    }
    else {
        reviewsStr = 'No reviews yet';
    }

    modal.innerHTML = `<p>Address: <span id="modalAddress">${details.formatted_address || 'N/A'}</span></p>
                        <p>Phone number: <span id="modalPhone">${details.formatted_phone_number || 'N/A'}</span></p>
                        <p>Int. phone number: <span id="modalIntPhone">${details.international_phone_number || 'N/A'}</span></p>
                        <p>Rating: <span id="modalRating">${details.rating || 'N/A'}</span></p>
                        <p>Opening hours: <span id="modalOpenings">${(details.opening_hours && details.opening_hours.periods[0].open && details.opening_hours.periods[0].open.time) ? details.opening_hours.periods[0].open.time : '0000'} - ${(details.opening_hours && details.opening_hours.periods[0].close && details.opening_hours.periods[0].close.time) ? details.opening_hours.periods[0].close.time : '0000'}</span></p>

                        ${reviewsStr}`;

    document.getElementById('mapModalLabel').innerHTML = details.name || 'N/A';
    $("#modalGoogle").attr("href", details.url || '#');
    $("#modalWebsite").attr("href", details.website || '#');
    $("#modalBtn").click();
}