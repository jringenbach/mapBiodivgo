/* Instanciation of the map */
var map = new OpenLayers.Map('mapDiv');
map.addLayer(new OpenLayers.Layer.OSM());
map.zoomToMaxExtent();

/* Instanciation of markers' layer and properties of markers*/
var markers = new OpenLayers.Layer.Markers("Markers");
var size = new OpenLayers.Size(21,25);
var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);
var icon = new OpenLayers.Icon('https://www.google.fr/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjwt8vZ45TVAhVH8RQKHX_MBVgQjRwIBw&url=http%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fmap-marker_33622&psig=AFQjCNG5Lg-D-UKXayB1ycxxsCrS-3bJbA&ust=1500534211043837', size, offset);

/*Listener qui va contenir les évènements associés au click sur le linestring */
var layerListeners = {
    //Quand on clique sur le LineString
    featureclick: function(e) {
        return false;
    },

    nofeatureclick: function(e) {
    }
};

/* Creation of a geoJSON object */
var geoJSONLineString = new OpenLayers.Format.GeoJSON({
            'internalProjection': new OpenLayers.Projection("EPSG:3857"),
            'externalProjection': new OpenLayers.Projection("EPSG:4326")
        });

//Creation of a vector layer
var vector = new OpenLayers.Layer.Vector("geoJSON", {
           projection: new OpenLayers.Projection("EPSG: 4326"),
        });

var indexOfLineStringSelected;
var lineStringUser = null;
var tableOfLineStringUser = createTableOfLineStringEneo(tableOfLineString, geoJSONLineString);
console.log(tableOfLineStringUser[0]["features"]);
addFeaturesToVectorLayer(vector, tableOfLineStringUser);
map.addLayer(vector);

/**
 * Event fired with a click on a map. The linestring feature will be check in order to know if it is selected or not.
 */
map.events.register("click", map, function(e){

    indexOfLineStringSelected = testLineStringFeatureClickedOn(e, vector);
    console.log("indexOfLineString : "+indexOfLineStringSelected);
    //If the LineString feature has been clicked on by the user
    if(indexOfLineStringSelected != null){
        lineStringUser = tableOfLineStringUser[indexOfLineStringSelected];

        //If the LineStringEneo hasn't been selected yet
        if(!lineStringUser.isSelected){

            //Instanciation of the event of the first marker
            lineStringUser.markerStart.marker.events.register("click", lineStringUser.markerStart.marker, function(e){
                lineStringUser.markerStartIsSelected(true);
            });

            //Instanciation of the event of the second marker
            lineStringUser.markerEnd.marker.events.register("click", lineStringUser.markerEnd.marker, function(e){
                lineStringUser.markerStartIsSelected(false);
            });

            //We add the markers to the map
            lineStringUser.addMarkersToMap(markers, map);

            lineStringUser.isSelected = true;
        }

        //If a LineString is already selected
        else{

            //We get the position of the click on the map (with x;y coordinates => EPSG:3857)
            var lonlat = map.getLonLatFromViewPortPx(e.xy);

            //If the markerStart is selected
            if(lineStringUser.markerStart.isSelected && !lineStringUser.markerEnd.isSelected){
                lineStringUser.markerStart.moveMarker(markers, lonlat);         
            }

            //If markerEnd is selected, we move it
            else if(lineStringUser.markerEnd.isSelected && !lineStringUser.markerStart.isSelected){
                lineStringUser.markerEnd.moveMarker(markers, lonlat);  
            }

            //We get the coordinates properties from the LineString
            var coordinatesLineString = lineStringUser.features[0]["geometry"]["components"];

            //We change the projection of markers to set point in EPSG4326 because turf work with those values
            lineStringUser.changeProjectionOfMarkers("EPSG:3857", "EPSG:4326");

            //Instanciation of the points that will work with turf library
            var pointStart = InstanciateGeoJSONPoint(lineStringUser.markerStart.marker);
            var pointEnd = InstanciateGeoJSONPoint(lineStringUser.markerEnd.marker);

            //point***Index represent the point where we will know the index of the segment of the linestring where the markers are
            var pointStartIndex = turf.pointOnLine(tableOfLineString[indexOfLineStringSelected], pointStart, "kilometers");
            var pointEndIndex = turf.pointOnLine(tableOfLineString[indexOfLineStringSelected], pointEnd, "kilometers");

            console.log("index start : "+pointStartIndex["properties"]["index"]);
            console.log("index end : "+pointEndIndex["properties"]["index"]);
            
            if(pointStartIndex["properties"]["index"] > pointEndIndex["properties"]["index"]){
                var temp = pointStartIndex;
                pointStartIndex = pointEndIndex;
                pointEndIndex = temp;
            }

            //If markers are on a different segment of the LineString
            if(pointStartIndex["properties"]["index"] != pointEndIndex["properties"]["index"]){
                tableOfLineString[indexOfLineStringSelected]["geometry"]["coordinates"].splice(pointStartIndex["properties"]["index"]+1, 0, pointStartIndex["geometry"]["coordinates"]);
                tableOfLineString[indexOfLineStringSelected]["geometry"]["coordinates"].splice(pointEndIndex["properties"]["index"]+2, 0, pointEndIndex["geometry"]["coordinates"]);

                var distanceTotale = calculateDistanceSliced(tableOfLineString[indexOfLineStringSelected]["geometry"]["coordinates"], pointStartIndex["properties"]["index"]+1, pointEndIndex["properties"]["index"]+2);
                
                //On retire les markers des coordonnées du geojson maintenant que les calculs sont finis
                tableOfLineString[indexOfLineStringSelected]["geometry"]["coordinates"].splice(pointStartIndex["properties"]["index"]+1, 1);
                tableOfLineString[indexOfLineStringSelected]["geometry"]["coordinates"].splice(pointEndIndex["properties"]["index"]+1, 1);
            }

            //If both markers are on the same segment of the LineString
            else{
                var distanceTotale = turf.distance(pointStart, pointEnd, "kilometers");
            }

            //We reproject the markers with EPSG:3857 norm
            lineStringUser.changeProjectionOfMarkers("EPSG:4326", "EPSG:3857");
            metersOrKilometers(distanceTotale);


        }//End of "else" of "LineString" is Selected
    } //End of if(indexOfLineStringSelected != null)
});

/**
 * Add all the features to a vector layer
 * @param {*An OpenLayers.Layer.Vector object} vector 
 * @param {*Table with all the LineStringEneo object} tableOfLineStringEneo 
 */
function addFeaturesToVectorLayer(vector, tableOfLineStringEneo){
    for(var i=0; i<tableOfLineStringEneo.length; i++){
        vector.addFeatures(tableOfLineStringEneo[i].features);       
    }
}

/**
 * Calculate a serie of distance between 2 geojson points using turf library
 * @param {*Coordinates of a point} coordinates 
 * @param {*First index in the table of coordinates} startIndex 
 * @param {*Last index in the table of coordinates} EndIndex 
 */
function calculateDistanceSliced(coordinates, startIndex, EndIndex){
    var distanceTotale = 0;
    var latlng1, latlng2;

    for(var i=startIndex; i<EndIndex-1; i++){ 
        var from = {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Point",
                    "coordinates": coordinates[i]
            }
        };

        var to = {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Point",
                    "coordinates": coordinates[i+1]
            }
        };

          distanceTotale += turf.distance(from, to, "kilometers");
          console.log(i+" : "+distanceTotale);
    }

    return distanceTotale;
}

/**
 * Create a table of LineStringEneo object
 * @param {*Table filled with all the linestring features of the user} tableOfLineString 
 * @param {*An OpenLayers.Format.geoJSON object that will serialize the features } geoJSONLineString
 */
function createTableOfLineStringEneo(tableOfLineString, geoJSONLineString){
    var tableOfLineStringEneo = new Array();
    for(var i=0; i<tableOfLineString.length; i++){
        tableOfLineStringEneo.push(new LineStringEneo(geoJSONLineString.read(tableOfLineString[i]), false, null, null));
    }

    return tableOfLineStringEneo;
}

function metersOrKilometers(distance){
    if(!(distance > 1.0)){
        console.log("Distance totale : "+distance*1000+" m");
    }
    else console.log("Distance totale : "+distanceTotale+" km");
}

/**
 * Instanciate a Point feature with the coordinates of a marker
 * @param {*Marker used to set the coordinates of the Point feature} marker 
 */
function InstanciateGeoJSONPoint(marker){
    var point = {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        marker.lonlat.lon,
                        marker.lonlat.lat
                        ]
                }
    };

    return point;
}

function testLineStringFeatureClickedOn(event, vector){
    for(var i=0; i<vector["features"].length; i++){
        console.log("---- "+i+" ----");
        console.log(event["target"]["_featureId"]);
        console.log(vector["features"][i]["id"]);

        if(event["target"]["_featureId"] == vector["features"][i]["id"]){
            return i;
        }
    }

    console.log("retourne null");
    return null;
}



