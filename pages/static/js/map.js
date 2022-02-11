function initMap() {
    let walk_lat = document.getElementById("walk-lat").innerHTML;
    let walk_lng = document.getElementById("walk-lng").innerHTML;  
    let walk_lat_float = parseFloat(walk_lat);
    let walk_lng_float = parseFloat(walk_lng);
    const location = { lat: walk_lat_float, lng: walk_lng_float };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 11,
        center: location,
    });
    const marker = new google.maps.Marker({
        position: location,
        map: map,
    });

    // alert(walk_lat)

}