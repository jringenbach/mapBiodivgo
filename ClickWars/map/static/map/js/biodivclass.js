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
 * @param {*Booléen valant true si le défi est réalisable l'été} summer
 * @param {*T} typeChallenge
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

    //Icone lié au type de défi
    this.iconChallenge;

    //Marker lié à l'icone du type de défi
    this.marker;

    //Selon le type de challenge, on instancie un icone différent qui sera associé à un marqueur leaflet
    switch(this.typeChallenge.typeName){
        case "insecte":
            this.iconChallenge = L.icon({
                iconUrl: '../static/map/img/insect.png',
                iconSize:     [36, 36], // size of the icon
                iconAnchor:   [18, 36], // point of the icon which will correspond to marker's location
                popupAnchor:  [-76, -10] // point from which the popup should open relative to the iconAnchor
            });
        break;

        case "animal":
            this.iconChallenge = L.icon({
                iconUrl: '../static/map/img/animal.png',
                iconSize:     [36, 36], // size of the icon
                iconAnchor:   [18, 36], // point of the icon which will correspond to marker's location
                popupAnchor:  [-76, -10] // point from which the popup should open relative to the iconAnchor
            });
        break;

        case "flore":
                this.iconChallenge = L.icon({
                iconUrl: '../static/map/img/flower.png',
                iconSize:     [36, 36], // size of the icon
                iconAnchor:   [18, 36], // point of the icon which will correspond to marker's location
                popupAnchor:  [-76, -10] // point from which the popup should open relative to the iconAnchor
            });
        break;
    }

    //On égalise la position du marqueur avec le centre du cercle de la zone de défi
    this.marker = L.marker([this.circle.getLatLng().lat,this.circle.getLatLng().lng], {icon : this.iconChallenge});

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
function typeChallenge(idType, typeName){
    this.idType = idType;
    this.typeName = typeName;
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

