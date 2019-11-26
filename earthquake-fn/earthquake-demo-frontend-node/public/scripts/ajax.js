var events_endpoint = "/events";
var mapTitles;
var minMeasure = 0;

function getEndpoint(type) {
  url = events_endpoint;
  if (type != "")
    url +=  "?type=" + type;
  return url;
}

$(document).ready(function() {

  $.ajax({
    url: getEndpoint($("#type").find(":selected").val()), 
    method: 'GET',
    success: mapSuccess,
    error: mapError
  });

  $("#find").submit(function(event) {
    event.preventDefault();
    $.ajax({
      url: getEndpoint($("#type").find(":selected").val()),
      method: 'GET',
      success: remap,
      error: mapError
    });
  });

  // Sort by measure
  function sortEvents(response) {
     var sorted = response.sort(function(a, b) {
       return (a.measure > b.measure) ? -1 : ((b.measure > a.measure) ? 1 : 0)
     });

     return sorted;
  }

  function initMap(response, minMeasure) {
    var map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 37.78, lng: -122.44},
      zoom: 2
    });
    for(let i = 0; i < response.length; i++){
      minMeasure = $(".measure").val();
      var measure = response[i].measure;
      if(measure >= minMeasure) {
        var latLng = new google.maps.LatLng(response[i].lat,response[i].lon);
        var image = {
          url: './images/' + response[i].type + '.png',
          size: new google.maps.Size(20, 32),
          origin: new google.maps.Point(0, 0),
          anchor: new google.maps.Point(0, 32),
          scaledSize: new google.maps.Size(25, 25)
        };
        var marker = new google.maps.Marker({
          position: latLng,
          map: map,
          icon: image,
        });
      };
    };
  };

  function mapSuccess(response) {
    response = sortEvents(response);
    for(let i = 0; i < response.length; i++){
      mapTitles = JSON.parse(response[i].address).address
      id = response[i].id
      var measure = parseFloat(response[i].measure).toFixed(2);
      var type = response[i].type;
      $('#info').append(`<p id=${id}> <span class="type">${type}</span> (${measure}) ${mapTitles} </p>`)
    };
    initMap(response, minMeasure);
    console.log(response);
  };

  function mapError(error1, error2, error3) {
    console.log(error1);
    console.log(error2);
    console.log(error3);
  };

  function remap(response) {
    response = sortEvents(response);
    $("#info").empty();
    minMeasure = $(".measure").val();
    for(let i = 0; i < response.length; i++){
      mapTitles = JSON.parse(response[i].address).address
      id = response[i].id
      var measure = parseFloat(response[i].measure).toFixed(2);
      var type = response[i].type;
      if(measure >= minMeasure) {
        $('#info').append(`<p id=${id}> <span class="type">${type}</span> (${measure}) ${mapTitles} </p>`)
      };
    };
    initMap(response, minMeasure);
    console.log(response);
  }
});