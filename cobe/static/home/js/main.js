let map = L.map('mapid').setView([48.15797, 11.57542], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicG11bGFyY3p5ayIsImEiOiJja2J6YTMyZ3AwOXByMnVtcmpqZjhwYmVmIn0.lT1Xsu8H6axbDmxRl2Dwaw'
}).addTo(map);

// Target's GPS coordinates.
const target = L.latLng('48.15797', '11.57542');

// Set map's center to target with zoom 14.
map.setView(target, 14);

// Place a marker on the same location.
L.marker(target).addTo(map);