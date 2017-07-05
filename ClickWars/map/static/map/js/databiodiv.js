/*-----------------------------------------------------------------------------------------------
                                        INSTANCIATION DES CHALLENGES
-------------------------------------------------------------------------------------------------*/

/*Instanciation : nom, description, circle, autumn, spring, summer, winter  */
var beziersChallenge = new Challenge(
    "Y'a de la vie à Béziers?",
    "Trouve un semblant de vie à Béziers",
    beziersCercle,
    true,
    false,
    false,
    true
);

var juvignacChallenge = new Challenge(
    "Si juvignac, c'est juvamine",
    "Trouve une pêche à Juvignac",
    juvignacCercle,
    true,
    false,
    false,
    true
);

var mirevalChallenge = new Challenge(
    "Mireval Valhala",
    "Où te caches-tu petite coccinelle de mon enfance?",
    mirevalCercle,
    true,
    true,
    true,
    false
);

var montpellierChallenge = new Challenge(
    "Montpellier, ma bichette!",
    "Une biche se cache dans montpellier. Sauras-tu la trouver?",
    montpellierCercle,
    true,
    true,
    true,
    true
);

var palavasChallenge = new Challenge(
    "Palavas-les-fleurs",
    "Trouve la fameuse jonquille de Palavas-les-Flots",
    palavasCercle,
    false,
    false,
    false,
    true
);

var perolsChallenge = new Challenge(
    "Pérock'n roll",
    "Un pétunia? Quel pétunia?",
    perolsCercle,
    false,
    true,
    true,
    false
);

var pignanChallenge = new Challenge(
    "Mon père, Pignan!",
    "Trouvez un coquelicot dans Pignan",
    pignanCercle,
    false,
    true,
    true,
    true
);

var seteChallenge = new Challenge(
    "Sète à la maison",
    "Mais où se cachent les algues de Sète?",
    seteCercle,
    true,
    false,
    true,
    false
);

var saintJeanDeVedasChallenge = new Challenge(
    "Las Védas 21",
    "Prêt à photographier les guêpes de Védas?",
    saintJeanDeVedasCercle,
    false,
    true,
    true,
    false
);

var villeneuveMagueloneChallenge = new Challenge(
    "Le vieux Villeneuve",
    "As-tu vu le scarabée de villeneuve?",
    villeneuveMagueloneCercle,
    true,
    true,
    true,
    true
);

var tableauDeChallenges = new Array();
tableauDeChallenges.push(beziersChallenge);
tableauDeChallenges.push(juvignacChallenge);
tableauDeChallenges.push(mirevalChallenge);
tableauDeChallenges.push(montpellierChallenge);
tableauDeChallenges.push(palavasChallenge);
tableauDeChallenges.push(perolsChallenge);
tableauDeChallenges.push(pignanChallenge);
tableauDeChallenges.push(saintJeanDeVedasChallenge);
tableauDeChallenges.push(seteChallenge);
tableauDeChallenges.push(villeneuveMagueloneChallenge);

/*-----------------------------------------------------------------------------------------------
                                        INSTANCIATION DES JOUEURS
-------------------------------------------------------------------------------------------------*/

//Création d'un icône de ninja
var ninjaIcon = L.icon({
    iconUrl: '../static/map/img/ninja.png',
    iconSize:     [36, 36], // size of the icon
    iconAnchor:   [18, 36], // point of the icon which will correspond to marker's location
    popupAnchor:  [-76, -10] // point from which the popup should open relative to the iconAnchor
});

//Création d'un marqueur que l'on associe à l'icône du ninja
var marker = L.marker([43.611051565377174, 3.876843452453613], {icon: ninjaIcon});
var markerDorian = L.marker([43.58238046828168, 3.764190673828125], {icon: ninjaIcon});
var markerDylan = L.marker([43.65594991256823, 3.8874435424804688], {icon: ninjaIcon});
var markerJohnny = L.marker([43.64924291736786, 3.8544845581054683], {icon: ninjaIcon});
var markerFred = L.marker([43.641665595900456, 3.8538408279418945], {icon: ninjaIcon});
var markerSophie = L.marker([43.64105999003001, 3.852370977401733], {icon: ninjaIcon});
var markerAntoine = L.marker([43.64217802686894, 3.852928876876831], {icon: ninjaIcon});
var markerGerald = L.marker([43.64097458358277,3.855053186416626], {icon: ninjaIcon});
var markerAsterix = L.marker([43.53212261888178,3.860492706298828], {icon: ninjaIcon});
var markerLuffy = L.marker([43.56820304329252,3.8287353515624996], {icon: ninjaIcon});

//INSTANCIATION DES JOUEURS
var joueur = new Player("Julien", marker, ninjaIcon);
var dorian = new Player("Dorian_la_kikoune", markerDorian, ninjaIcon);
var dylan = new Player("Thug-life-34", markerDylan, ninjaIcon);
var johnny = new Player("Biker34", markerJohnny, ninjaIcon);
var fred = new Player("StapsFred", markerFred, ninjaIcon);
var sophie = new Player("FanDeBieber", markerSophie, ninjaIcon);
var antoine = new Player("Tony-l-embrouille", markerAntoine, ninjaIcon);
var gerald = new Player("Codeur-de-lextreme", markerGerald, ninjaIcon);
var asterix = new Player("Astérix", markerAsterix, ninjaIcon);
var luffy = new Player("Luffy", markerLuffy, ninjaIcon);

var playersTable = new Array();

playersTable.push(dorian);
playersTable.push(dylan);
playersTable.push(johnny);
playersTable.push(fred);
playersTable.push(sophie);
playersTable.push(antoine);
playersTable.push(gerald);
playersTable.push(asterix);
playersTable.push(luffy);

/*-----------------------------------------------------------------------------------------------
                                        INSTANCIATION DES CHECKBOX
-------------------------------------------------------------------------------------------------*/


//On instance les checkbox
//checkbox a coché si le joueur veut voir les joueurs proches de lui
var checkboxNearestPlayers = document.getElementById("nearestPlayersCheckBox");
var checkboxNearestChallenge = document.getElementById("nearestChallengeCheckBox");
var checkboxChallengeDescription = document.getElementById("challengeDescriptionCheckBox");
var checkboxPopUpChallenge = document.getElementById("popUpCheckBox");
var checkboxWinter = document.getElementById("winterCheckBox");
var checkboxSpring = document.getElementById("springCheckBox");
var checkboxSummer = document.getElementById("summerCheckBox");
var checkboxAutumn = document.getElementById("autumnCheckBox");

//Instanciation des boutons
var buttonToutCocher = document.getElementById("toutCocherButton");
var buttonToutDecocher = document.getElementById("toutDecocherButton");

console.log("winter : "+checkboxWinter);
//Ajout des checkbox dans un tableau
var checkboxArray = new Array();
checkboxArray.push(checkboxNearestPlayers);
checkboxArray.push(checkboxNearestChallenge);
checkboxArray.push(checkboxChallengeDescription);
checkboxArray.push(checkboxPopUpChallenge);
checkboxArray.push(checkboxWinter);
checkboxArray.push(checkboxSpring);
checkboxArray.push(checkboxSummer);
checkboxArray.push(checkboxAutumn);

