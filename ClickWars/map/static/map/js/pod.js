var lineStringToSlice = 
 {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            3.758697509765625,
            43.537598280094535
          ],
          [
            3.7998962402343746,
            43.632099415557754
          ],
          [
            3.8960266113281254,
            43.59928952130085
          ],
          [
            3.7902832031250004,
            43.66886497805366
          ],
          [
            3.6625671386718746,
            43.58039085560784
          ],
          [
            3.755950927734375,
            43.48082639482503
          ],
          [
            4.010009765624999,
            43.64104446159409
          ]
        ]
      }
    };


//Premier marker d'un linestring sur la carte
var markerStart;

//Second marker d'un linestring sur la carte
var markerEnd;

var isLineStringSelected = false;
var isMarkerStartSelected = false;
var isMarkerEndSelected = false;

var styleMouseOver = {color : "yellow"};
var initialStyleLineString = {color : "blue"};
var styleClickLineString = {color : "red"};
var slicedStyle = {color : "green"};





//Création de la carte
var map = L.map('mapDiv').setView([43.611051565377174, 3.876843452453613], 13);

//Création de la couche de tuiles qui est ajoutée à la map
L.tileLayer('https://api.mapbox.com/styles/v1/foxof/cj4jxxmvx7gwp2rs5571l8z3o/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZm94b2YiLCJhIjoiY2ozeTJ0a3hjMDAwcTJ3bGJwMHFyMWtrbSJ9.rsjnfathrl-cGADOA7P1zg').addTo(map);

var geoJSONLineString = L.geoJSON(lineStringToSlice).addTo(map);

//Evènement se déclenchant quand la souris survole le linestring
geoJSONLineString.on("mouseover", function(e){
  if(!isLineStringSelected) e.target.setStyle(styleMouseOver);

});

//On change le style dés que la souris quitte le LineString
geoJSONLineString.on("mouseout", function(e){
  if(!isLineStringSelected) e.target.setStyle(initialStyleLineString);
});

//Evènement qui se déclenche au click sur le LineString
geoJSONLineString.on("click", function(e){
    e.target.setStyle(styleClickLineString);
    if(!isLineStringSelected){

      var lengthTabCoordinates = lineStringToSlice["geometry"]["coordinates"].length;

      //On créé les latitudes et longitudes des markers qui seront aux extrémités du linestring
      var latlngStart = L.latLng(lineStringToSlice["geometry"]["coordinates"][0][1], lineStringToSlice["geometry"]["coordinates"][0][0]);
      var latlngEnd = L.latLng(lineStringToSlice["geometry"]["coordinates"][lengthTabCoordinates-1][1], 
                              lineStringToSlice["geometry"]["coordinates"][lengthTabCoordinates-1][0]);

      //On créé les markers
      markerStart = L.marker(latlngStart).addTo(map);
      markerEnd = L.marker(latlngEnd).addTo(map);

      isLineStringSelected = true;

      markerStart.on("click", function(e){
        isMarkerStartSelected = true;
        isMarkerEndSelected = false;
      });

      markerEnd.on("click", function(e){
        isMarkerStartSelected = false;
        isMarkerEndSelected = true;
      });
    }

    else{
        if(isMarkerStartSelected && !isMarkerEndSelected){
            markerStart.setLatLng(e.latlng);
        }

        else if(isMarkerEndSelected && !isMarkerStartSelected){
            markerEnd.setLatLng(e.latlng);
        }

        var pointStart ={
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                          "type": "Point",
                          "coordinates": [
                            markerStart.getLatLng().lng,
                            markerStart.getLatLng().lat
                          ]
                        }
                      };

        var pointEnd ={
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                          "type": "Point",
                          "coordinates": [
                            markerEnd.getLatLng().lng,
                            markerEnd.getLatLng().lat
                          ]
                        }
                      };

        /*Insérer les points dans le lineString */
        var pointStartIndex = turf.pointOnLine(lineStringToSlice, pointStart, "kilometers");
        var pointEndIndex = turf.pointOnLine(lineStringToSlice, pointEnd, "kilometers");

        console.log("index start : "+pointStartIndex["properties"]["index"]);
        console.log("index end : "+pointEndIndex["properties"]["index"]);
        
        if(pointStartIndex["properties"]["index"] > pointEndIndex["properties"]["index"]){
            var temp = pointStartIndex;
            pointStartIndex = pointEndIndex;
            pointEndIndex = temp;
        }
        console.log(pointStartIndex);
        if(pointStartIndex["properties"]["index"] != pointEndIndex["properties"]["index"]){
            lineStringToSlice["geometry"]["coordinates"].splice(pointStartIndex["properties"]["index"]+1, 0, pointStartIndex["geometry"]["coordinates"]);
            lineStringToSlice["geometry"]["coordinates"].splice(pointEndIndex["properties"]["index"]+2, 0, pointEndIndex["geometry"]["coordinates"]);

            var distanceTotale = calculateDistanceSliced(lineStringToSlice["geometry"]["coordinates"], pointStartIndex["properties"]["index"]+1, pointEndIndex["properties"]["index"]+2);
            lineStringToSlice["geometry"]["coordinates"].splice(pointStartIndex["properties"]["index"]+1, 1);
            lineStringToSlice["geometry"]["coordinates"].splice(pointEndIndex["properties"]["index"]+1, 1);
        }

        else{
            var latlng1 = L.latLng(pointStartIndex["geometry"]["coordinates"][1], pointStartIndex["geometry"]["coordinates"][0]);
            var latlng2 = L.latLng(pointEndIndex["geometry"]["coordinates"][1], pointEndIndex["geometry"]["coordinates"][0]);
            var distanceTotale = latlng1.distanceTo(latlng2);
        }


        console.log("Distance : "+distanceTotale+" mètres");

    }


});

function clone(obj) {
    if (null == obj || "object" != typeof obj) return obj;
    var copyObject = obj.constructor();
    for (var attr in obj) {
        if (obj.hasOwnProperty(attr)) copyObject[attr] = obj[attr];
    }
    return copyObject;
}

function calculateDistanceSliced(coordinates, startIndex, EndIndex){
    var distanceTotale = 0;
    var latlng1, latlng2;

    for(var i=startIndex; i<EndIndex-1; i++){
          latlng1 = L.latLng(coordinates[i][1], coordinates[i][0]);
          latlng2 = L.latLng(coordinates[i+1][1], coordinates[i+1][0]);
          distanceTotale += latlng1.distanceTo(latlng2);
          console.log(i+" : "+distanceTotale);
    }

    return distanceTotale;
}
