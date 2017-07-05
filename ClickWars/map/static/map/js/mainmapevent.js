//On stocke dans une variable le bouton cible qui sera déclencheur de l'évènement
var loadTilesButton = document.getElementById("loadTilesButton");


var boundaryGeomIsOn = true;

//On lie l'évènement onclick à la méthode loadEveryTiles
loadTilesButton.onclick = loadEveryTiles;

/**
 * Méthode appelée par un évènement lié à un bouton qui va modifier la couche de tuiles utilisée
 * par la carte. Soit l'utilisateur affiche une couche avec toutes les tuiles de la carte, soit il 
 * affiche une couche comprenant seulement les tuiles qui sont à l'intérieur du polygone.
 */
function loadEveryTiles(){
    console.log("LoadTilesButtonFired");

    //On retire la couche n'affichant que les tuiles à l'intérieur du polygone
    //et on affiche toutes les tuiles de la carte
    if(boundaryGeomIsOn){
        mymap.removeLayer(boundaryGeom);
        allTilesLayer.addTo(mymap);
        boundaryGeomIsOn = false;
    }

    //On arrête d'afficher toutes les tuiles de la carte et on affiche que les tuiles
    //dans le polygone
    else{
        mymap.removeLayer(allTilesLayer);
        boundaryGeom.addTo(mymap);
        boundaryGeomIsOn = true;
    }

}

