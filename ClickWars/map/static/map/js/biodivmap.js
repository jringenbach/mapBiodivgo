/*-----------------------------------------------------------------------------------------------
                                        INSTANCIATION DES VARIABLES
-------------------------------------------------------------------------------------------------*/

//On instancie la carte
var map = L.map('mapDiv').setView([43.611051565377174, 3.876843452453613], 13);
var messageBoxNumberOfPlayersNearYouIsOnScreen = false;

//Instanciation du message indiquant le nombre de joueurs présent autour du joueur principal
var optionMessageBoxPlayerNearYou = {timeout : 3000, position : "topright"};
var messageBoxPlayerNearYou = L.control.messagebox(optionMessageBoxPlayerNearYou).addTo(map);

//Instanciation du message indiquant le challenge le plus proche
var optionMessageBoxNearestChallenge = {timeout : 2000, position : "bottomleft"};
var messageBoxNearestChallenge = L.control.messagebox(optionMessageBoxNearestChallenge).addTo(map);

//Options du messagebox qui affiche la description d'un défi quand le joueur est dans une zone de défi
var optionMessageBox = {timeout : 3000, position : "bottomright"};
var messageBoxDescriptionChallenge = L.control.messagebox(optionMessageBox).addTo(map);

//On créé une couche de tuiles avec l'adresse de notre style personnalisé
L.tileLayer('https://api.mapbox.com/styles/v1/foxof/cj4jxxmvx7gwp2rs5571l8z3o/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZm94b2YiLCJhIjoiY2ozeTJ0a3hjMDAwcTJ3bGJwMHFyMWtrbSJ9.rsjnfathrl-cGADOA7P1zg').addTo(map);


//On ajoute le marker du joueur à la carte, ainsi que celui de tous les autres joueurs

var ampleurDuDeplacement = 0.001; //Ampleur du déplacement du joueur
textboxVitMainCharacter.value = ampleurDuDeplacement;
joueur.marker.addTo(map);
textboxZoomLevel.value = map.getZoom();
textBoxCoordinatesMainCharacter(joueur.marker);
removeOrAddPlayersMarker(playersTable, map);

var challengeDisplayed = new Array();
challengeDisplayed = displayChallengeZone(tableauDeChallenges, challengeDisplayed, map, joueur.marker);

//-------------------------------------------------------------------------------------------

/*-----------------------------------------------------------------------------------------------
                                            EVENEMENTS
-------------------------------------------------------------------------------------------------*/
document.addEventListener('keydown', function(e){
    var insideAChallengeZone;

    //Si la touche appuyée concerne un déplacement
    if(e.keyCode == 68 || e.keyCode == 90 || e.keyCode == 83 || e.keyCode == 81){
        switch(e.keyCode){

            //Left - Q key
            case 81:
                latitude = joueur.marker.getLatLng().lat;
                longitude = joueur.marker.getLatLng().lng-Math.abs(ampleurDuDeplacement);
                break;
            
            //Up - Z key
            case 90:
                latitude = joueur.marker.getLatLng().lat+Math.abs(ampleurDuDeplacement);
                longitude = joueur.marker.getLatLng().lng;
            break;

            //Right - D key
            case 68:
                latitude = joueur.marker.getLatLng().lat;
                longitude = joueur.marker.getLatLng().lng+Math.abs(ampleurDuDeplacement);
                break;

            //Down - S key
            case 83:
                latitude = joueur.marker.getLatLng().lat-Math.abs(ampleurDuDeplacement);
                longitude = joueur.marker.getLatLng().lng;
                break;
            
        }

        //On modifie la position du marqueur, on teste si le joueur est dans une zone de défi, si il y'a des joueurs autour
        //de lui
        joueur.marker.setLatLng([latitude, longitude]);
        textBoxCoordinatesMainCharacter(joueur.marker);
        insideAChallengeZone = markerIsInsideChallengeZone(joueur.marker, challengeDisplayed);

        //si le joueur a coché la checkbox pour voir les joueurs les plus proches, alors on calcule la distance des joueurs les plus proches
        if(checkboxNearestPlayers.checked){
            playerIsNearAnOtherPlayer(joueur, playersTable);
        }

        if(!insideAChallengeZone) nearestChallenge(joueur, tableauDeChallenges);

        //On recentre la carte sur le marqueur du joueur principal
        map.setView(joueur.marker.getLatLng(), map.getZoom());

    }

});

/**
 * Coche toutes les checkbox du menu des options
 */
buttonToutCocher.addEventListener("click", function(e){
    checkOrUncheckAllCheckBox(checkboxArray, true);
    removeOrAddPlayersMarker(playersTable, map);
    challengeDisplayed = displayChallengeZone(tableauDeChallenges, challengeDisplayed, map, joueur.marker);
});

/**
 * Décoche toutes les checkbox du menu des options
 */
buttonToutDecocher.addEventListener("click", function(e){
    checkOrUncheckAllCheckBox(checkboxArray, false);
    removeOrAddPlayersMarker(playersTable, map);
    checkOrUncheckCheckBoxPopUpChallenge();
    challengeDisplayed = displayChallengeZone(tableauDeChallenges, challengeDisplayed, map, joueur.marker);
});

/**
 * Evènement lié à la checkbox affichant les joueurs les plus proches.
 * On supprime les joueurs de la carte quand elle est décochée.
 */
checkboxNearestPlayers.addEventListener("change", function(e){
    removeOrAddPlayersMarker(playersTable, map);
});

/**
 * Evènement lié à la check demandant si on autorise l'affichage d'un popup avec le nom du défi
 * au-dessus du personnage
 */
checkboxPopUpChallenge.addEventListener("change", function(e){
    checkOrUncheckCheckBoxPopUpChallenge();
});

/**
 * Evènement lié quand la checkbox winter est cochée/décochée
 */
checkboxWinter.addEventListener("change", function(e){
    challengeDisplayed = displayChallengeZone(tableauDeChallenges, challengeDisplayed, map, joueur.marker);
});

/**
 * Evènement lié quand la checkbox spring est cochée/décochée
 */
checkboxSpring.addEventListener("change", function(e){
    challengeDisplayed = displayChallengeZone(tableauDeChallenges, challengeDisplayed, map, joueur.marker);
});

/**
 * Evènement lié quand la checkbox summer est cochée/décochée
 */
checkboxSummer.addEventListener("change", function(e){
    challengeDisplayed = displayChallengeZone(tableauDeChallenges, challengeDisplayed, map, joueur.marker);
});

/**
 * Evènement lié quand la checkbox autumn est cochée/décochée
 */
checkboxAutumn.addEventListener("change", function(e){
    challengeDisplayed = displayChallengeZone(tableauDeChallenges, challengeDisplayed, map, joueur.marker);
});

/**
 * Evènement se déclenchant quand le niveau de zoom change. On va redimensionner les icones des types de défi.
 */
map.addEventListener("zoomstart", function(e){
    var icon;

    for(var i = 0; i < challengeDisplayed.length; i++){
        //On retire un à un les marqueurs des défis de la carte
        map.removeLayer(challengeDisplayed[i].marker);

        //Pour un défi, on récupère son icone suivant le niveau de zoom de la carte
        icon = getIconDependingOnZoomLevel(map.getZoom(), challengeDisplayed[i].typeChallenge.typeName);

        //On affiche l'icone
        challengeDisplayed[i].marker.setIcon(icon);
        challengeDisplayed[i].marker.addTo(map);
    }

});

/**
 * Evènement quand l'animation d'un zoom se termine
 */
map.addEventListener("zoomend", function(e){
    //Dans les statistiques, on met à jour le niveau de zoom
    textboxZoomLevel.value = map.getZoom();
});

/**
 * textbox permettant de modifier la vitesse du personnage principal sur la carte
 */
textboxVitMainCharacter.addEventListener("change", function(e){

    //Si l'utilisateur essaie d'entrer une vitesse négative
    if(textboxVitMainCharacter.value <= 0 ){
        textboxVitMainCharacter.style.borderColor = "red";
    }

    else{
        textboxVitMainCharacter.style.borderColor = "#015651";
        ampleurDuDeplacement = textboxVitMainCharacter.value;
    }

});


/*-----------------------------------------------------------------------------------------------
                                        METHODES
-------------------------------------------------------------------------------------------------*/

/**
 * Ajoute à la carte les zones de défi dont la zone de défi est un cercle
 * @param {*Tableau contenant les challenges à afficher sur la carte} challengeDisplayed
 * @param {*La carte} map 
 */
function addChallengeZoneToMap(challengeDisplayed, map){

    //On parcourt le tableau de challenge à afficher pour ajouter les couches une à une à la carte
    for(var i=0; i < challengeDisplayed.length; i++){
        challengeDisplayed[i].circle.addTo(map);
    }
}

/**
 * Ajoute les marqueurs des joueurs sur la carte
 * @param {*Tableau contenant tous les jours} playersTable 
 */
function addMarkerPlayersOnMap(playersTable, map){
    for(var i=0; i<playersTable.length; i++){
        playersTable[i].marker.addTo(map);
    }
}

/**
 * Ajoute chaque couche contenant un polygone à la carte
 * @param {*Tableau contenant chaque couche avec un polygone par couche} polygonsLayers 
 * @param {*La carte} map 
 */
function addPolygonLayersToMap(polygonsLayers, map){
    for(var i = 0; i < polygonsLayers.length; i++){
        polygonsLayers[i].addTo(map);
    }
}

/**
 * Ajoute les marqueurs relatifs au type de défi
 * @param {*Tableau contenant les défis à afficher selon les options choisies} challengeDisplayed 
 * @param {*La carte } map 
 */
function addTypeChallengeMarkerToMap(challengeDisplayed, map){
    for(var i=0; i<challengeDisplayed.length; i++){
        challengeDisplayed[i].marker.addTo(map);
    }
}

/**
 * Calcul le challenge le plus prôche
 * @param {*Le joueur principal} player 
 * @param {*Le tableau contenant les challenges} challengeArray 
 */
function calculNearestChallenge(player, challengeArray){
    var challengeLePlusProche;
    var distanceMin, distance, message;
    for(var i=0; i<challengeArray.length; i++){
        distance = joueur.marker.getLatLng().distanceTo(challengeArray[i].circle.getLatLng());
        distance -= challengeArray[i].circle.getRadius();

        //Pour le premier tour de boucle, on ne fait pas de test on récupère juste le challenge et la distance avec ce challenge
        if(i==0){
            challengeLePlusProche = challengeArray[i];
            distanceMin = distance;
        }

        else{
            //On regarde si la distance entre le joueur et le challenge actuel est inférieur à la distance minimale
            //enregistrée pour un challenge 
            if(distance < distanceMin){
                challengeLePlusProche = challengeArray[i];
                distanceMin = distance;
            }
        }
    }
    //Si la distance minimale est inférieure à 0, alors on est dans une zone de défi et on affichera pas de message
    if(distanceMin<0) message = "AlreadyInChallenge";

    //Sinon on va afficher le message
    else{

        //Si la distance est supérieur à 1000m, on l'affiche en kilomètre
        if(distanceMin>1000) message = challengeLePlusProche.challengeName+" : "+(distanceMin/1000).toFixed(4)+"km";
        //Sinon on l'affiche en mètres
        else message = challengeLePlusProche.challengeName + " : "+distanceMin.toFixed(0)+"m";
    } 

    //On renvoie le message à afficher dans la messagebox
    return message;
}

/**
 * Ajoute un popup au marqueur avec le nom du défi quand le joueur est dans une zone de défi
 * @param {*Indice du tableau contenant les cercles des zones de défi} circleNumber
 * @param {*Tableau contenant les défis qui vont être affichés} challengeDisplayed
 */
function challengePopUp(circleNumber, challengeDisplayed){
    var messagePopUp;

    //Contenu du popup qui s'affiche au-dessus du joueur.
    messagePopUp = "Défi : "+ challengeDisplayed[circleNumber]["challengeName"];
    joueur.marker.bindPopup(messagePopUp).openPopup();


}

/**
 * Permet de changer la couleur du cercle de la zone de défi quand le joueur est dedans
 * @param {*Indice du tableau contenant les cercles des zones de défi} circleNumber
 * @param {*Tableau contenant tous les défis à afficher} challengeDisplayed
 */
function changeColorCircle(circleNumber, challengeDisplayed){

        challengeDisplayed[circleNumber].circle.setStyle(styleMarkerIsInside);
}

/**
 * Décoche ou coche toutes les checkbox
 * @param {*Tableau contenant toutes les checkbox} checkboxArray 
 * @param {*Booléen valant true si tout doit être coché et false si tout doit être décoché} checkBoolean 
 */
function checkOrUncheckAllCheckBox(checkboxArray, checkBoolean){
    //On parcourt le tableau de checkbox pour toutes les cocher/décocher selon la valeur de checkBoolean
    for(var i=0; i<checkboxArray.length; i++){
        checkboxArray[i].checked = checkBoolean;
    }  
}

/**
 * On vérifie si la checkbox pour le popup du nom du défi est coché ou non. On affiche ou non le popup en conséquence
 */
function checkOrUncheckCheckBoxPopUpChallenge(){
    //Si la case est décochée, on enlève le pop-up si il existe
    if(!checkboxPopUpChallenge.checked){
        joueur.marker.closePopup();
    }

    //Si la case est cochée, on va vérifier que le joueur est bien dans une zone de défi, et si oui, on affiche le pop up
    else{
        var inside = markerIsInsideCircle(joueur.marker, challengeDisplayed);
        challengePopUp(inside["which"], challengeDisplayed);
    }
}

/**
 * Créé un tableau dont chaque case contient une couche liée à un polygone. Renvoie un tableau
 * contenant une couche par case
 * @param {*tableau contenant tous les défis} challengesTab
 */
function createPolygonsLayers(challengesTab){
    numberOfLayers = challengesTab.length;
    var features;
    var polygonsLayers = new Array();

    //Pour les features de chaque challenge, on va créer une couche
    for(var i=0; i<numberOfLayers; i++){
        if(challengesTab[i]["geoJSONChallenge"] != null){
            features = challengesTab[i]["geoJSONChallenge"]["features"];
            polygonsLayers.push(L.geoJSON(features));
        }

    }

    return polygonsLayers;
}

/**
 * Ajoute dans un tableau de couches, tous les défis qui ont pour zone géographique un cercle
 * @param {*Tableau contenant tous les défis} challengesTab 
 */
function createChallengeZone(challengesTab){
    var challengesDisplayed = new Array();

    for(var i=0; i < challengesTab.length; i++){
        if(challengesTab[i].circle != null &&(
           (checkboxWinter.checked == true && checkboxWinter.checked == challengesTab[i].winter) ||
           (checkboxSpring.checked == true && checkboxSpring.checked == challengesTab[i].spring) ||
           (checkboxSummer.checked == true && checkboxSummer.checked == challengesTab[i].summer) ||
           (checkboxAutumn.checked == true && checkboxAutumn.checked == challengesTab[i].autumn))){
                challengesDisplayed.push(challengesTab[i]); //Si la propriété cercle n'est pas nulle, on l'ajoute au tableau
        }
    }

    return challengesDisplayed;
}

/**
 * Regroupement des méthodes indiquant quelles couches de zones de défi doivent être affichées sur la carte
 * @param {*Tableau contenant tous les défis} tableauDeChallenges 
 * @param {*Tableau contenant toutes les couches dessinant les zones de défi} challengeDisplayed
 * @param {*La carte} map
 * @param {*Le marqueur du joueur} markerPlayer
 */
function displayChallengeZone(tableauDeChallenges, challengeDisplayed, map, markerPlayer){
    //On retire tous les cercles de zone de défi de la carte
    if(challengeDisplayed.length > 0) removeAllChallengeZoneFromMap(challengeDisplayed, map);

    //On recalcule les cercles que l'on doit afficher
    challengeDisplayed = createChallengeZone(tableauDeChallenges);

    //On ajoute les zones de défi à la carte
    addChallengeZoneToMap(challengeDisplayed, map);

    //On ajoute les marqueurs relatifs au type de défi
    addTypeChallengeMarkerToMap(challengeDisplayed, map);

    //On leur attribue une couleur
    instanciateColorPolygons(challengeDisplayed, markerPlayer);
    return challengeDisplayed;
}

/**
 * Renvoie l'url de l'image à afficher pour l'icone
 * @param {*Type du challenge} challengeType 
 */
function getIconDependingOnChallengeType(challengeType){
    var iconUrl;

    switch(challengeType){
        case "insecte":
            iconUrl = '../static/map/img/insect.png'
        break;

        case "animal":
            iconUrl = '../static/map/img/animal.png'
        break;

        case "flore":
            iconUrl = '../static/map/img/flower.png'
        break;
    }

    return iconUrl;
}

/**
 * Renvoie un icone selon le niveau de zoom sur la carte
 * @param {*Niveau du zoom} zoomlevel
 * @param {*Type du challenge} challengeType
 */
function getIconDependingOnZoomLevel(zoomlevel, challengeType){
    var icon, iconUrl, anchorIcon;
    var sizeIcon = new Array();

    //Suivant le niveau de zoom, l'icone aura une taille et un point d'ancrage différent
    if(zoomlevel >= 13){
        sizeIcon = [36,36];
        anchorIcon = [18,36];
    } 

    else if(zoomlevel >= 10){
        sizeIcon = [18,18];
        anchorIcon = [9,16];
    } 

    else if(zoomlevel >= 5){
        sizeIcon = [8,8];
        anchorIcon = [4, 8];
    } 

    else{
        sizeIcon = [3,3];
        anchorIcon = [1, 0];
    } 

    //Suivant le type du défi, l'icone aura une image différente
    iconUrl = getIconDependingOnChallengeType(challengeType);

    icon = L.icon({
                iconUrl: iconUrl,
                iconSize: sizeIcon, // size of the icon
                iconAnchor: anchorIcon, // point of the icon which will correspond to marker's location
                popupAnchor:  [-76, -10] // point from which the popup should open relative to the iconAnchor
    });

    return icon;
}

/**
 * Instancie la couleur des polygones au chargement de la page
 * @param {*} polygonsLayers 
 * @param {*} marker
 */
function instanciateColorPolygons(challengeDisplayed, marker){

    //On colore d'abord chaque polygone en rouge
    for(var i=0; i < challengeDisplayed.length; i++){
        challengeDisplayed[i].circle.setStyle(styleMarkerNotInside);
    }

    //Ensuite on regarde si le marqueur a été instancié sur un polygone
    //Si oui, on le colorie en bleu
    markerIsInsideChallengeZone(marker, challengeDisplayed);

}

/**
 * Permet d'inverser les coordonnées à l'intérieur d'un tableau contenant les coordonnées de plusieurs points.
 * Inversion de la latitude et de la longitude dans le tableau
 * @param {*Tableau contenant les coordonnées de 1 ou plusieurs points} tableau 
 */
function inverserCoordonneesTableau(tableau){
    var temp = 0;
    for(var i = 0; i<tableau.length; i++){
        temp = tableau[i][0];
        tableau[i][0] = tableau[i][1];
        tableau[i][1] = temp;
    }

    return tableau;
}

/**
 * Calcule si le marqueur est dans un polygone, et si oui, change sa couleur
 * @param {* Marqueur : objet} marker 
 * @param {* Tableau contenant les défis à afficher} challengeDisplayed
 */
function markerIsInsideChallengeZone(marker, challengeDisplayed){

    inside = markerIsInsideCircle(marker, challengeDisplayed);

    //Si le joueur est dans une zone de défi
    if(inside["isInside"]){
        changeColorCircle(inside["which"], challengeDisplayed);
        //Si la checkbox pour afficher la description est cochée
        if(checkboxChallengeDescription.checked) showDescriptionChallenge(inside["which"], challengeDisplayed);

        //Si la checkbox pour afficher le nom du défi en pop-up est coché
        if(checkboxPopUpChallenge.checked)challengePopUp(inside["which"], challengeDisplayed);
    }

    else{
        //Pour chaque zone de défi, on redéfinit la couleur associée à l'absence du joueur dans une zone de défi
        for(var i = 0; i < challengeDisplayed.length; i++){
            challengeDisplayed[i].circle.setStyle(styleMarkerNotInside);
            joueur.marker.closePopup();
        }
    }

    return inside["isInside"];
}

/**
 * Teste si le personnage est à l'intérieur d'une zone de défi en cercle ou non
 * @param {*Marqueur représentant le personnage} marker 
 * @param {*Tableau contenant tous les défis à afficher} challengeDisplayed
 */
function markerIsInsideCircle(marker, challengeDisplayed){
    var inside = {
                isInside : false,
                which : -1
            };

    for(var i = 0; i < challengeDisplayed.length; i++){
        if(marker.getLatLng().distanceTo(challengeDisplayed[i].circle.getLatLng())<challengeDisplayed[i].circle.getRadius()){
            inside = {
                isInside : true,
                which : i
            };
        }
    }

    return inside;
}

/**
 * Teste si un point est à l'intérieur d'un polygone. Si oui, elle renvoie "true"
 * @param {* Coordonnées d'un point (Array)} point 
 * @param {* Liste des points composant un polygone(Array of coordinates)} polygon 
 */
function markerIsInsidePolygon(point, polygon){
    var inside = false;
    var i = 0;
    var pointTable = [point.getLatLng().lng, point.getLatLng().lat];
    var turfPoint = turf.point(pointTable);
    var turfPolygon;

    var insideWhichPolygon = new Object();

    //On recherche dans cette boucle dans quel polygone se trouve le marqueur
    do{
        turfPolygon = turf.polygon(polygon[i]);
        if(turf.inside(turfPoint, turfPolygon)) inside = true;
        i++;
    }while(i<polygon.length && inside == false);

    i--; //On décrémente i pour retomber sur le bon polygone

    insideWhichPolygon = {
            isInside : inside,
            polygon : true,
            circle : false,
            which : i
        };

    return insideWhichPolygon;
}
/**
 * Regroupe les méthodes de calcul du challenge le plus prôche et de l'affichage de la messagebox indiquant quel challenge c'est
 * @param {*Le joueur principal} joueur 
 * @param {*Tableau de challenges} challengeArray 
 */
function nearestChallenge(joueur, challengeArray){
    var message = calculNearestChallenge(joueur, challengeArray);

    //Si le joueur n'est pas déjà dans une zone de défi et si il a coché la checkbox indiquant
    //qu'il voulait voir le défi le plus proche dans les options, alors on affiche le défi le plus prôche
    if(message != "AlreadyInChallenge" && checkboxNearestChallenge.checked){
        messageBoxNearestChallenge.show(message);
    }
}

/**
 * Teste si un joueur est prôche du joueur principal
 * @param {*Le joueur sur son application} player 
 * @param {*Les autres joueurs qu'il peut rencontrer} playersTable 
 */
function playerIsNearAnOtherPlayer(player, playersTable){
    var nearPlayers = new Array();
    var numberOfPlayersNearYou = 0;
    var positionMainPlayer = player.marker.getLatLng();
    var positionOtherPlayer = 0.0;
    var message = "";
    for(var i=0; i < playersTable.length; i++){
        positionOtherPlayer = playersTable[i].marker.getLatLng();
        if(positionMainPlayer.distanceTo(positionOtherPlayer) < 1000.0){
            nearPlayers[numberOfPlayersNearYou] = playersTable[i];
            numberOfPlayersNearYou++;           
        }
    }

    //Si le nombre de joueurs prôches est supérieur à 0, on va afficher un message sur la carte avec le plugin messagebox de leaflet
    if(numberOfPlayersNearYou > 0){
        message = showPlayerNearYou(nearPlayers);
        messageBoxPlayerNearYou.show(message);
    }

}

/**
 * Retire toutes les couches qui dessinent les cercles des zones de défi
 * @param {* Tableau contenant tous les défis à afficher} challengeDisplayed
 * @param {* La carte} map 
 */
function removeAllChallengeZoneFromMap(challengeDisplayed, map){
    for(var i=0; i < challengeDisplayed.length; i++){
        //On retire le cercle représentant la zone de défi
        map.removeLayer(challengeDisplayed[i].circle);

        //On retire l'icone représentant le type du défi
        map.removeLayer(challengeDisplayed[i].marker);
    }
}

/**
 * Suivant si la checkbox qui demande à l'utilisateur si il veut afficher les joueurs les plus proches ou non est cochée ou décochée
 * On ajoute les marqueurs des joueurs à la carte ou on les retire
 * @param {*Tableau contenant les joueurs autres que le personnage principal} playersTable 
 * @param {*La carte} map 
 */
function removeOrAddPlayersMarker(playersTable, map){
    //Si la checkbox est décochée, on retire les joueurs de la carte
    if(!checkboxNearestPlayers.checked){
        removePlayersMarkerFromMap(playersTable, map);
    }

    //Si elle est cochée, on ajoute les joueurs sur la carte
    else{
        addMarkerPlayersOnMap(playersTable, map); 
    }
}

/**
 * On retire les marqueurs des joueurs de la carte
 * @param {*Tableau contenant tous les joueurs sauf le joueur principal} playersTable 
 * @param {*La carte} map 
 */
function removePlayersMarkerFromMap(playersTable, map){
    for(var i=0; i<playersTable.length; i++){
        map.removeLayer(playersTable[i].marker);
    }
}

/**
 * Affiche la description du défi quand le joueur est dans une zone de défi
 * @param {*Position de la zone de défi dans le tableau des couches de défi} circleNumber
 * @param {*Tableau contenant les défis à afficher} challengeDisplayed 
 */
function showDescriptionChallenge(circleNumber, challengeDisplayed){
    messageBoxDescriptionChallenge.show(challengeDisplayed[circleNumber].description);
}

function showPlayerNearYou(nearPlayers){
    var message = new String();

    for(var i=0; i<3; i++){
        //Si c'est le dernier joueur de la liste, on ne met pas la virgule après le pseudo
        if (i == nearPlayers.length-1) message = message.concat(nearPlayers[i].pseudo);

        //Sinon, on affiche le pseudo suivi d'une virgule
        else if(i < nearPlayers.length-1){
            message = message.concat(nearPlayers[i].pseudo);
            message = message.concat(", ");
        } 
    }

    if(nearPlayers.length == 1) message += " est prêt de toi";
    else if(nearPlayers.length <4 ) message += " sont prêts de toi";
    else{
        message += " et ";
        
        if(nearPlayers.length-3 == 1) message+=" 1 autre joueur sont prêts de toi";
        else message += (nearPlayers.length-3)+" autres joueurs sont prêts de toi";
    } 

    return message;
}

/**
 * Affiche la latitude du joueur dans la textbox du panel "Données et Statistiques"
 * @param {*Marqueur du joueur} markerPlayer 
 */
function textBoxCoordinatesMainCharacter(markerPlayer){
    textboxLatMainCharacter.value = markerPlayer.getLatLng().lat;
    textboxLonMainCharacter.value = markerPlayer.getLatLng().lng;
}



