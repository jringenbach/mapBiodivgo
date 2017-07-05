/**
 * jsonToTiles permet à partir d'un geojson d'obtenir l'adresse de toutes les tuiles pour des niveaux de zoom donnés
 * @param {*Objet "geometry" d'un objet geojson} polygonjson 
 */
function jsonToTiles(polygonjson){
    polyjsonstring = JSON.stringify(polygonjson);
    polyjsonparse = JSON.parse(polyjsonstring);

    /*On récupère le module node tile-cover*/
    var cover = require('@mapbox/tile-cover');

    /*On définit le zoom minimum et le zoom maximum */
    var limits = {
        min_zoom: 2,
        max_zoom: 16
    };

    /* On utilise la méthode tiles du module node tiles-cover qui permet de donner toutes les tuiles pour chaque niveau de 
    zoom qui recouvrent le polygone */
    var tilesRaw = cover.tiles(polyjsonparse, limits);

    for(var i=0; i<tilesRaw.length; i++){
            var x = tilesRaw[i][0];
            var y = tilesRaw[i][1];
            var z = tilesRaw[i][2];
            tileUrl = "http://{s}.tile.openstreetmap.org/"+z+"/"+x+"/"+y+".png";
            tileUrl = tileUrl.replace("{s}.", "");
            console.log(i+" : "+tileUrl);
    }
}




