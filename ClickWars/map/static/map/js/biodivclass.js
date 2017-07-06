var tableauDeChallenges = new Array();

/**
 * Classe représentant un joueur
 * @param {*Pseudo du joueur} pseudo 
 * @param {*Marqueur leaflet affiché sur la carte pour représenter le joueur} marker 
 * @param {*Icone utilisé pour afficher le joueur sur la carte} icon 
 */
function Player(pseudo, marker, icon){
    this.pseudo = pseudo;
    this.marker = marker;
    this.icon = icon;
}


/**
 * Classe représentant les défis de biodivgo
 * @param {*Nom du défi} challengeName 
 * @param {*Description du défi} description
 * @param {*Zone du défi (circulaire)} circle 
 * @param {*Booléen valant true si le défi est réalisable au printemps } spring
 * @param {*Booléen valant true si le défi est réalisable en automne} autumn
 * @param {*Booléen valant true si le défi est réalisable en hiver} winter
 * @param {*ZBooléen valant true si le défi est réalisable l'été} summer 
 */
function Challenge(challengeName, description, circle, autumn, spring, summer, winter, typeChallenge){
    this.challengeName = challengeName;
    this.description = description;
    this.circle = circle;
    this.geoJSON = circleToGeoJSON(circle);
    this.spring = spring;
    this.autumn = autumn;
    this.winter = winter;
    this.summer = summer;
    this.typeChallenge = typeChallenge;
    tableauDeChallenges.push(this);
    
    /**
     * Transforme un geoJSON en un tableau contenant les tableaux de coordonnées de chaque polygone
     */
    this.geoJSONToTable = function(){
        var tableauDeCoordonnees = new Array();

        if(this.geoJSONChallenge != null){
            //Si un geoJSON contient plusieurs polygones, alors on les récupèrera tous
            for(var i=0; i < this.geoJSONChallenge["features"][0]["geometry"]["coordinates"].length; i++){
                tableauDeCoordonnees.push(this.geoJSONChallenge["features"][0]["geometry"]["coordinates"][i]);
            }
        }

        return tableauDeCoordonnees;
    };


}

/**
 * Type de défis
 * @param {*Identifiant du type de défi} idType 
 * @param {*Nom du type de défi} typeName 
 */
function typeChallenge(idType, typeName, marker){
    this.idType = idType;
    this.typeName = typeName;
    this.marker = marker;
}

/**
* Transforme un objet cercle issu de leaflet en un geoJSON personnalisé (le cercle n'existant pas dans les normes geoJSON)
*/
function circleToGeoJSON(circle){
        var geoJSON = {
                "type": "FeatureCollection",
                "features": [
                        {
                        "type": "Feature",
                        "properties": {
                            "type": "Circle",
                            "radius" : circle.getRadius().toString()
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [
                            circle.getLatLng().Lat,
                            circle.getLatLng().Lng
                            ]
                        }
                    }
            ]
        };

    return geoJSON;
};

