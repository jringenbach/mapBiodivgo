/**
 * Désigne les marqueurs aux extrémités d'un linestring
 */
class LineStringMarker{
    /**
     * 
     * @param {*OpenLayers.Marker Object displayable on a map} marker 
     * @param {*Boolean that is equal to true if the marker is clicked on} isSelected 
     */
    constructor(marker, isSelected) {
        this.marker = marker;
        this.isSelected = isSelected;
    }

    getIsSelected(){
        return this.isSelected;
    }

    getMarker(){
        return this.marker;
    }

    setMarker(marker){
        this.marker = marker;
    }

    setIsSelected(isSelected){
       if(typeof isSelected == "boolean") this.isSelected = isSelected;
    }

    //************************************************************************************************************
    //                                          METHODES DE LINESTRINGMARKER
    //************************************************************************************************************

    /**
     * Change the projection of the marker
     * @param {*Actual projection of the marker} fromProjection 
     * @param {*Desired projection of the marker} toProjection 
     */
    changeProjectionOfMarker(fromProjection, toProjection){
        this.marker.lonlat.transform(new OpenLayers.Projection(fromProjection), new OpenLayers.Projection(toProjection));
        console.log("change projection of marker");
        console.log(this.marker);
    }

    /**
     * Move a marker to a new latitude and longitude
     * @param {*Layer where markers will be displayed} markers 
     * @param {*An OpenLayers LonLat - New latitude and longitude where the marker will be moved} lonlat 
     */
    moveMarker(markers, lonlat){
        this.marker.lonlat = new OpenLayers.LonLat(lonlat.lon, lonlat.lat);
        markers.removeMarker(this.marker);
        markers.addMarker(this.marker);
        markers.redraw();
    }
}

/**
 * Object containing the LineString and both markers defining its extremities
 */
class LineStringEneo{

    /**
     * Constructeur de LineStringENeo
     * @param {*Geometric figure displayable on a map} features 
     * @param {*OpenLayers marker at the first extremity of the Linestring(features)} markerStart 
     * @param {*OpenLayers marker at the second extremity of the Linestring(features)} markerEnd 
     */
    constructor(features, isSelected, markerStart, markerEnd){
        this.features = features;
        this.isSelected = isSelected;
        this.markerStart = markerStart;
        this.markerEnd = markerEnd;

        this.instanciateMarkers(this.features[0]["geometry"]["components"][0]["x"], this.features[0]["geometry"]["components"][0]["y"]);
        var lengthCoordinates = this.features[0]["geometry"]["components"].length;
        this.instanciateMarkers(this.features[0]["geometry"]["components"][lengthCoordinates-1]["x"], this.features[0]["geometry"]["components"][lengthCoordinates-1]["y"]);

    }

    /**
     * Getters for isSelected
     */
    getIsSelected(){
        return this.isSelected;
    }

    /**
     * Getters for markerStart
     */
    getMarkerStart(){
        return this.markerStart;
    }

    /**
     * Getters for markerEnd
     */
    getMarkerEnd(){
        return this.markerEnd;
    }

    /**
     * Setters for isSelected
     * @param {*Boolean equals to true if the LineString has been clicked on} isSelected 
     */
    setIsSelected(isSelected){
        if(typeof isSelected === "boolean") this.isSelected = isSelected;
    }

    /**
     * Setters for markerStart
     * @param {*Marker at the first extremity of the LineString} markerStart 
     */
    setMarkerStart(markerStart){
        this.markerStart = markerStart;
    }

    /**
     * Setters for markerEnd
     * @param {*Marker at the second extremity of the LineString} markerEnd 
     */
    setMarkerEnd(markerEnd){
        this.markerEnd = markerEnd;
    }

    /**
     * Setters for both markers of the LineString
     * @param {*Marker at the first extremity of the LineString} markerStart 
     * @param {*Marker at the second extremity of the LineString} markerEnd 
     */
    setMarkers(markerStart, markerEnd){
        this.markerStart = markerStart;
        this.markerEnd = markerEnd;
    }

    //************************************************************************************************************
    //                                          METHODES DE LINESTRINGENEO
    //************************************************************************************************************

    /**
     * Add markerStart and markerEnd to a map through a layer of markers OpenLayers.Markers
     * @param {*Layer of markers : OpenLayers.Markers} markers 
     * @param {*The map where the markers will be displayed} map 
     */
    addMarkersToMap(markers, map){
            markers.addMarker(this.markerStart.marker);
            markers.addMarker(this.markerEnd.marker);
            map.addLayer(markers);
    }

    /**
     * Change the projection of markerStart and markerEnd
     * @param {*Actual projection of the marker} fromProjection 
     * @param {*Desired projection of the marker} toProjection 
     */
    changeProjectionOfMarkers(fromProjection, toProjection){
        this.markerStart.changeProjectionOfMarker(fromProjection, toProjection);
        this.markerEnd.changeProjectionOfMarker(fromProjection, toProjection);
    }

    /**
     * Instanciate a LineStringMarker. If none of the markers have been instanciate, markerStart is instanciated first.
     * @param {*marker's longitude} lon 
     * @param {*marker's latitude} lat 
     */
    instanciateMarkers(lon, lat){

        var lonLatMarker = new OpenLayers.LonLat(lon, lat);
        if(this.markerStart == null && this.markerEnd == null){
            var pointMarker = new OpenLayers.Marker(lonLatMarker, icon);
            this.markerStart = new LineStringMarker(pointMarker, false);
        }

        else {
            var pointMarker = new OpenLayers.Marker(lonLatMarker, icon.clone());
            this.markerEnd = new LineStringMarker(pointMarker, false);
        } 
    }

    /**
     * Define the boolean of the markers depending on which one has been clicked on
     * @param {*Boolean equals to true if markerStart has been clicked on. False if markerEnd has been clicked on} startIsSelected 
     */
    markerStartIsSelected(startIsSelected){
        if(startIsSelected){
            this.markerStart.isSelected = true;
            this.markerEnd.isSelected = false;
        }

        else{
            this.markerStart.isSelected = false;
            this.markerEnd.isSelected = true;            
        }

    }



}
