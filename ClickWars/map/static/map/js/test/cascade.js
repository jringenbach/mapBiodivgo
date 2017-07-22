var d2r = Math.PI / 180,
    r2d = 180 / Math.PI;

/****************************************************************************************************************** */
/*                                                  TILE-COVER                                                      */
/****************************************************************************************************************** */

/**
 * Permet de récupérer les coordonnées des tuiles suivant le type de geometry qui est envoyé
 */
function getTiles(geom, limits) {
    var i, tile,
        coords = geom.coordinates,
        maxZoom = limits.max_zoom,
        tileHash = {},
        tiles = [];

    if (geom.type === 'Point') {
        return [pointToTile(coords[0], coords[1], maxZoom)];

    } else if (geom.type === 'MultiPoint') {
        for (i = 0; i < coords.length; i++) {
            tile = pointToTile(coords[i][0], coords[i][1], maxZoom);
            tileHash[toID(tile[0], tile[1], tile[2])] = true;
        }
    } else if (geom.type === 'LineString') {
        lineCover(tileHash, coords, maxZoom);

    } else if (geom.type === 'MultiLineString') {
        for (i = 0; i < coords.length; i++) {
            lineCover(tileHash, coords[i], maxZoom);
        }
    } else if (geom.type === 'Polygon') {
        polygonCover(tileHash, tiles, coords, maxZoom);

    } else if (geom.type === 'MultiPolygon') {
        for (i = 0; i < coords.length; i++) {
            polygonCover(tileHash, tiles, coords[i], maxZoom);
        }
    } else {
        throw new Error('Geometry type not implemented');
    }

    if (limits.min_zoom !== maxZoom) {
        // sync tile hash and tile array so that both contain the same tiles
        var len = tiles.length;
        appendHashTiles(tileHash, tiles);
        for (i = 0; i < len; i++) {
            var t = tiles[i];
            tileHash[toID(t[0], t[1], t[2])] = true;
        }
        return mergeTiles(tileHash, tiles, limits);
    }

    appendHashTiles(tileHash, tiles);
    return tiles;
}

/**
 * Méthode utilisée dans getTiles
 * @param {*} hash 
 * @param {*} tiles 
 */
function appendHashTiles(hash, tiles) {
    var keys = Object.keys(hash);
    for (var i = 0; i < keys.length; i++) {
        tiles.push(fromID(+keys[i]));
    }
}

/**
 * Calcule les tuiles recouvrant une ligne
 * @param {*} tileHash 
 * @param {*} coords 
 * @param {*} maxZoom 
 * @param {*} ring 
 */
function lineCover(tileHash, coords, maxZoom, ring) {
    var prevX, prevY;

    for (var i = 0; i < coords.length - 1; i++) {
        var start = pointToTileFraction(coords[i][0], coords[i][1], maxZoom),
            stop = pointToTileFraction(coords[i + 1][0], coords[i + 1][1], maxZoom),
            x0 = start[0],
            y0 = start[1],
            x1 = stop[0],
            y1 = stop[1],
            dx = x1 - x0,
            dy = y1 - y0;

        if (dy === 0 && dx === 0) continue;

        var sx = dx > 0 ? 1 : -1,
            sy = dy > 0 ? 1 : -1,
            x = Math.floor(x0),
            y = Math.floor(y0),
            tMaxX = dx === 0 ? Infinity : Math.abs(((dx > 0 ? 1 : 0) + x - x0) / dx),
            tMaxY = dy === 0 ? Infinity : Math.abs(((dy > 0 ? 1 : 0) + y - y0) / dy),
            tdx = Math.abs(sx / dx),
            tdy = Math.abs(sy / dy);

        if (x !== prevX || y !== prevY) {
            tileHash[toID(x, y, maxZoom)] = true;
            if (ring && y !== prevY) ring.push([x, y]);
            prevX = x;
            prevY = y;
        }

        while (tMaxX < 1 || tMaxY < 1) {
            if (tMaxX < tMaxY) {
                tMaxX += tdx;
                x += sx;
            } else {
                tMaxY += tdy;
                y += sy;
            }
            tileHash[toID(x, y, maxZoom)] = true;
            if (ring && y !== prevY) ring.push([x, y]);
            prevX = x;
            prevY = y;
        }
    }

    if (ring && y === ring[0][1]) ring.pop();
}

/**
 * Recouvre un polygone avec des les tuiles
 * @param {*} tileHash 
 * @param {*} tileArray 
 * @param {*} geom 
 * @param {*} zoom 
 */
function polygonCover(tileHash, tileArray, geom, zoom) {
    var intersections = [];

    for (var i = 0; i < geom.length; i++) {
        var ring = [];
        lineCover(tileHash, geom[i], zoom, ring);

        for (var j = 0, len = ring.length, k = len - 1; j < len; k = j++) {
            var m = (j + 1) % len;
            var y = ring[j][1];

            // add interesction if it's not local extremum or duplicate
            if ((y > ring[k][1] || y > ring[m][1]) && // not local minimum
                (y < ring[k][1] || y < ring[m][1]) && // not local maximum
                y !== ring[m][1]) intersections.push(ring[j]);
        }
    }

    intersections.sort(compareTiles); // sort by y, then x

    for (i = 0; i < intersections.length; i += 2) {
        // fill tiles between pairs of intersections
        y = intersections[i][1];
        for (var x = intersections[i][0] + 1; x < intersections[i + 1][0]; x++) {
            var id = toID(x, y, zoom);
            if (!tileHash[id]) {
                tileArray.push([x, y, zoom]);
            }
        }
    }
}

function compareTiles(a, b) {
    return (a[1] - b[1]) || (a[0] - b[0]);
}

function mergeTiles(tileHash, tiles, limits) {
    var mergedTiles = [];

    for (var z = limits.max_zoom; z > limits.min_zoom; z--) {

        var parentTileHash = {};
        var parentTiles = [];

        for (var i = 0; i < tiles.length; i++) {
            var t = tiles[i];

            if (t[0] % 2 === 0 && t[1] % 2 === 0) {
                var id2 = toID(t[0] + 1, t[1], z),
                    id3 = toID(t[0], t[1] + 1, z),
                    id4 = toID(t[0] + 1, t[1] + 1, z);

                if (tileHash[id2] && tileHash[id3] && tileHash[id4]) {
                    tileHash[toID(t[0], t[1], t[2])] = false;
                    tileHash[id2] = false;
                    tileHash[id3] = false;
                    tileHash[id4] = false;

                    var parentTile = [t[0] / 2, t[1] / 2, z - 1];

                    if (z - 1 === limits.min_zoom) mergedTiles.push(parentTile);
                    else {
                        parentTileHash[toID(t[0] / 2, t[1] / 2, z - 1)] = true;
                        parentTiles.push(parentTile);
                    }
                }
            }
        }

        for (i = 0; i < tiles.length; i++) {
            t = tiles[i];
            if (tileHash[toID(t[0], t[1], t[2])]) mergedTiles.push(t);
        }

        tileHash = parentTileHash;
        tiles = parentTiles;
    }

    return mergedTiles;
}

function toID(x, y, z) {
    var dim = 2 * (1 << z);
    return ((dim * y + x) * 32) + z;
}

function fromID(id) {
    var z = id % 32,
        dim = 2 * (1 << z),
        xy = ((id - z) / 32),
        x = xy % dim,
        y = ((xy - x) / dim) % dim;
    return [x, y, z];
}

/****************************************************************************************************************** */
/*                                                  TILE-BELT                                                 */
/****************************************************************************************************************** */


/**
 * Get the tile for a point at a specified zoom level
 *
 * @name pointToTile
 * @param {number} lon
 * @param {number} lat
 * @param {number} z
 * @returns {Array<number>} tile
 * @example
 * var tile = pointToTile(1, 1, 20)
 * //=tile
 */
function pointToTile(lon, lat, z) {
    var tile = pointToTileFraction(lon, lat, z);
    tile[0] = Math.floor(tile[0]);
    tile[1] = Math.floor(tile[1]);
    return tile;
}

/**
 * Get the precise fractional tile location for a point at a zoom level
 *
 * @name pointToTileFraction
 * @param {number} lon
 * @param {number} lat
 * @param {number} z
 * @returns {Array<number>} tile fraction
 * var tile = pointToTileFraction(30.5, 50.5, 15)
 * //=tile
 */
function pointToTileFraction(lon, lat, z) {
    var sin = Math.sin(lat * d2r),
        z2 = Math.pow(2, z),
        x = z2 * (lon / 360 + 0.5),
        y = z2 * (0.5 - 0.25 * Math.log((1 + sin) / (1 - sin)) / Math.PI);
    return [x, y, z];
}

/****************************************************************************************************************** */
/*                                                  CODE PERSO                                                */
/****************************************************************************************************************** */
var geometryPolygonMultiple = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              1.4350461959838867,
              43.586919026109854
            ],
            [
              1.4366769790649414,
              43.586919026109854
            ],
            [
              1.4366769790649414,
              43.587882648457935
            ],
            [
              1.4350461959838867,
              43.587882648457935
            ],
            [
              1.4350461959838867,
              43.586919026109854
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              1.4335012435913086,
              43.583437423271334
            ],
            [
              1.4347457885742188,
              43.583437423271334
            ],
            [
              1.4347457885742188,
              43.58430784285869
            ],
            [
              1.4335012435913086,
              43.58430784285869
            ],
            [
              1.4335012435913086,
              43.583437423271334
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              1.4316987991333008,
              43.57983126519667
            ],
            [
              1.4335012435913086,
              43.57945820203314
            ],
            [
              1.4332437515258787,
              43.58088826494042
            ],
            [
              1.4316987991333008,
              43.57983126519667
            ]
          ]
        ]
      }
    }
  ]
};

/**
 * Cette méthode permet de récupérer les éléments "geometry" d'un geojson
 * @param {*A geojson object} geojsonObject 
 */
function getGeometryFromJSON(geojsonObject){
    //On instancie un tableau qui va récupérer l'élément geometry de chaque polygone
    var geometryTable = new Array();

    //Pour chaque objet features du geojson, on va en récupérer les Object.geometry
    geojsonObject.features.forEach(function(element){
        geometryTable.push(element.geometry);
    });

    return geometryTable;
}

/**
 * Méthode permettant de récupérer les tuiles pour chaque élément "geometry" d'un geojson
 * @param {*Tableau contenant les éléments "geometry" d'un geojson} geometryTable 
 */
function tilesForEveryGeometry(geometryTable){
    var tileList = new Array();

    geometryTable.forEach(function(element){
        tileList = tileList.concat(tilesForEveryZoom(element));
    });

    return tileList;
}

/*Dans l'application myEneo, seuls trois niveaux de zoom sont utilisables par l'utilisateur */
function tilesForEveryZoom(polygon){
    var tileList = new Array();
    //Niveau de zoom : 12
    var limitszoom12 = {
            min_zoom: 14,
            max_zoom: 14
        };

    //Niveau de zoom : 14
    var limitszoom14 = {
            min_zoom: 16,
            max_zoom: 16
        };

    //Niveau de zoom : 16
    var limitszoom16 = {
            min_zoom: 18,
            max_zoom: 18
        };

    //On récupère l'adresse url des tuiles pour les 3 niveaux de zoom
    tileList = tileList.concat(jsonToTiles(polygon, limitszoom12));
    tileList = tileList.concat(jsonToTiles(polygon, limitszoom14)); //On a ajoute à la suite les tuiles du niveau de zoom 14
    tileList = tileList.concat(jsonToTiles(polygon, limitszoom16)); //On a ajoute à la suite les tuiles du niveau de zoom 16
    //On retourne la liste des tuiles pour les 3 niveaux de zoom
    return tileList;
}

/**
 * jsonToTiles permet à partir d'un geojson d'obtenir l'url de toutes les tuiles pour des niveaux de zoom donnés
 * @param {*Objet "geometry" d'un objet geojson} polygonjson 
 */
function jsonToTiles(polygonjson, limits){
    polyjsonstring = JSON.stringify(polygonjson);
    polyjsonparse = JSON.parse(polyjsonstring);

    /* On utilise la méthode tiles du module node tiles-cover qui permet de donner toutes les tuiles pour chaque niveau de 
    zoom qui recouvrent le polygone */
    var tilesRaw = getTiles(polyjsonparse, limits);
    var tileListForOneZoom = new Array();
    for(var i=0; i<tilesRaw.length; i++){
            var x = tilesRaw[i][0];
            var y = tilesRaw[i][1];
            var z = tilesRaw[i][2];
            tileUrl = "http://{s}.tile.openstreetmap.org/"+z+"/"+x+"/"+y+".png";
            tileUrl = tileUrl.replace("{s}.", "");
            tileListForOneZoom.push(tileUrl);
    }
    
    //On retourne la liste des tuiles pour ce niveau de zoom
    return tileListForOneZoom;
}
