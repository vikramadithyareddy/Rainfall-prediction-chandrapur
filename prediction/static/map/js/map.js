var map;
function initMap() {
  console.log("Initializing map.................")
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
    passive:true
  });
}
