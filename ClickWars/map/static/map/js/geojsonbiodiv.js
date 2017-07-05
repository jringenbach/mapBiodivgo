//Style du polygone quand le joueur est dedans
var styleMarkerIsInside = {
            fillColor: 'blue',
            weight: 2,
            opacity: 1,
            color: 'white',  //Outline color
            fillOpacity: 0.7
        };

//Style d'un polygone quand le joueur n'est pas dedans
var styleMarkerNotInside = {
            fillColor: 'red',
            weight: 2,
            opacity: 1,
            color: 'white',  //Outline color
            fillOpacity: 0.7
        };

var beziersCercle = L.circle([43.34240849996516, 3.2141876220703125], {
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 3000
});

var juvignacCercle = L.circle([43.61414318728638, 3.80950927734375], {
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 1250
});

var mirevalCercle = L.circle([43.50772499687011, 3.8005828857421875], {
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 1400     
});

var montpellierCercle = L.circle([43.61047672368098, 3.8778305053710933], {
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 4000 
});

var palavasCercle = L.circle([43.52876230788813,3.9298439025878906], {
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 1100
});

var perolsCercle = L.circle([43.56117527541571,3.9529323577880855],{
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 900
});


var pignanCercle = L.circle([43.58238046828168, 3.764190673828125], {
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 1000 
});

var seteCercle = L.circle([43.40342617874741,3.680934906005859], {
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 1850   
});

var saintJeanDeVedasCercle = L.circle([ 43.56820304329252,3.8287353515624996], {
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 1850   
});

var villeneuveMagueloneCercle = L.circle([43.53212261888178,3.860492706298828], {
    color : 'red',
    fillColor : '#f03',
    fillOpacity: 0.5,
    radius: 1850   
});