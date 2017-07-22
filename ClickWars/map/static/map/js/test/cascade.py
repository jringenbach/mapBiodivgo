__all__ = ['cascade']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['pointToTile', 'tilesForEveryGeometry', 'fromID', 'r2d', 'pointToTileFraction', 'geometryPolygonMultiple', 'toID', 'd2r', 'tilesForEveryZoom', 'polygonCover', 'jsonToTiles', 'appendHashTiles', 'getTiles', 'getGeometryFromJSON', 'compareTiles', 'lineCover', 'mergeTiles'])
@Js
def PyJsHoisted_pointToTile_(lon, lat, z, this, arguments, var=var):
    var = Scope({'this':this, 'lat':lat, 'lon':lon, 'arguments':arguments, 'z':z}, var)
    var.registers(['lat', 'tile', 'lon', 'z'])
    var.put('tile', var.get('pointToTileFraction')(var.get('lon'), var.get('lat'), var.get('z')))
    var.get('tile').put('0', var.get('Math').callprop('floor', var.get('tile').get('0')))
    var.get('tile').put('1', var.get('Math').callprop('floor', var.get('tile').get('1')))
    return var.get('tile')
PyJsHoisted_pointToTile_.func_name = 'pointToTile'
var.put('pointToTile', PyJsHoisted_pointToTile_)
@Js
def PyJsHoisted_pointToTileFraction_(lon, lat, z, this, arguments, var=var):
    var = Scope({'this':this, 'lat':lat, 'lon':lon, 'arguments':arguments, 'z':z}, var)
    var.registers(['z2', 'sin', 'lat', 'x', 'y', 'z', 'lon'])
    var.put('sin', var.get('Math').callprop('sin', (var.get('lat')*var.get('d2r'))))
    var.put('z2', var.get('Math').callprop('pow', Js(2.0), var.get('z')))
    var.put('x', (var.get('z2')*((var.get('lon')/Js(360.0))+Js(0.5))))
    var.put('y', (var.get('z2')*(Js(0.5)-((Js(0.25)*var.get('Math').callprop('log', ((Js(1.0)+var.get('sin'))/(Js(1.0)-var.get('sin')))))/var.get('Math').get('PI')))))
    return Js([var.get('x'), var.get('y'), var.get('z')])
PyJsHoisted_pointToTileFraction_.func_name = 'pointToTileFraction'
var.put('pointToTileFraction', PyJsHoisted_pointToTileFraction_)
@Js
def PyJsHoisted_toID_(x, y, z, this, arguments, var=var):
    var = Scope({'y':y, 'z':z, 'this':this, 'arguments':arguments, 'x':x}, var)
    var.registers(['y', 'dim', 'z', 'x'])
    var.put('dim', (Js(2.0)*(Js(1.0)<<var.get('z'))))
    return ((((var.get('dim')*var.get('y'))+var.get('x'))*Js(32.0))+var.get('z'))
PyJsHoisted_toID_.func_name = 'toID'
var.put('toID', PyJsHoisted_toID_)
@Js
def PyJsHoisted_jsonToTiles_(polygonjson, limits, this, arguments, var=var):
    var = Scope({'polygonjson':polygonjson, 'this':this, 'arguments':arguments, 'limits':limits}, var)
    var.registers(['polygonjson', 'i', 'x', 'limits', 'tileListForOneZoom', 'y', 'z', 'tilesRaw'])
    var.put('polyjsonstring', var.get('JSON').callprop('stringify', var.get('polygonjson')))
    var.put('polyjsonparse', var.get('JSON').callprop('parse', var.get('polyjsonstring')))
    var.put('tilesRaw', var.get('getTiles')(var.get('polyjsonparse'), var.get('limits')))
    var.put('tileListForOneZoom', var.get('Array').create())
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('tilesRaw').get('length')):
        try:
            var.put('x', var.get('tilesRaw').get(var.get('i')).get('0'))
            var.put('y', var.get('tilesRaw').get(var.get('i')).get('1'))
            var.put('z', var.get('tilesRaw').get(var.get('i')).get('2'))
            var.put('tileUrl', ((((((Js('http://{s}.tile.openstreetmap.org/')+var.get('z'))+Js('/'))+var.get('x'))+Js('/'))+var.get('y'))+Js('.png')))
            var.put('tileUrl', var.get('tileUrl').callprop('replace', Js('{s}.'), Js('')))
            var.get('tileListForOneZoom').callprop('push', var.get('tileUrl'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('tileListForOneZoom')
PyJsHoisted_jsonToTiles_.func_name = 'jsonToTiles'
var.put('jsonToTiles', PyJsHoisted_jsonToTiles_)
@Js
def PyJsHoisted_tilesForEveryZoom_(polygon, this, arguments, var=var):
    var = Scope({'this':this, 'polygon':polygon, 'arguments':arguments}, var)
    var.registers(['limitszoom14', 'limitszoom12', 'tileList', 'polygon', 'limitszoom16'])
    var.put('tileList', var.get('Array').create())
    PyJs_Object_14_ = Js({'min_zoom':Js(14.0),'max_zoom':Js(14.0)})
    var.put('limitszoom12', PyJs_Object_14_)
    PyJs_Object_15_ = Js({'min_zoom':Js(16.0),'max_zoom':Js(16.0)})
    var.put('limitszoom14', PyJs_Object_15_)
    PyJs_Object_16_ = Js({'min_zoom':Js(18.0),'max_zoom':Js(18.0)})
    var.put('limitszoom16', PyJs_Object_16_)
    var.put('tileList', var.get('tileList').callprop('concat', var.get('jsonToTiles')(var.get('polygon'), var.get('limitszoom12'))))
    var.put('tileList', var.get('tileList').callprop('concat', var.get('jsonToTiles')(var.get('polygon'), var.get('limitszoom14'))))
    var.put('tileList', var.get('tileList').callprop('concat', var.get('jsonToTiles')(var.get('polygon'), var.get('limitszoom16'))))
    return var.get('tileList')
PyJsHoisted_tilesForEveryZoom_.func_name = 'tilesForEveryZoom'
var.put('tilesForEveryZoom', PyJsHoisted_tilesForEveryZoom_)
@Js
def PyJsHoisted_polygonCover_(tileHash, tileArray, geom, zoom, this, arguments, var=var):
    var = Scope({'geom':geom, 'tileArray':tileArray, 'zoom':zoom, 'this':this, 'arguments':arguments, 'tileHash':tileHash}, var)
    var.registers(['m', 'geom', 'k', 'i', 'ring', 'intersections', 'j', 'x', 'tileArray', 'y', 'zoom', 'tileHash', 'id', 'len'])
    var.put('intersections', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('geom').get('length')):
        try:
            var.put('ring', Js([]))
            var.get('lineCover')(var.get('tileHash'), var.get('geom').get(var.get('i')), var.get('zoom'), var.get('ring'))
            #for JS loop
            var.put('j', Js(0.0))
            var.put('len', var.get('ring').get('length'))
            var.put('k', (var.get('len')-Js(1.0)))
            while (var.get('j')<var.get('len')):
                try:
                    var.put('m', ((var.get('j')+Js(1.0))%var.get('len')))
                    var.put('y', var.get('ring').get(var.get('j')).get('1'))
                    if ((((var.get('y')>var.get('ring').get(var.get('k')).get('1')) or (var.get('y')>var.get('ring').get(var.get('m')).get('1'))) and ((var.get('y')<var.get('ring').get(var.get('k')).get('1')) or (var.get('y')<var.get('ring').get(var.get('m')).get('1')))) and PyJsStrictNeq(var.get('y'),var.get('ring').get(var.get('m')).get('1'))):
                        var.get('intersections').callprop('push', var.get('ring').get(var.get('j')))
                finally:
                        var.put('k', (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('intersections').callprop('sort', var.get('compareTiles'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('intersections').get('length')):
        try:
            var.put('y', var.get('intersections').get(var.get('i')).get('1'))
            #for JS loop
            var.put('x', (var.get('intersections').get(var.get('i')).get('0')+Js(1.0)))
            while (var.get('x')<var.get('intersections').get((var.get('i')+Js(1.0))).get('0')):
                try:
                    var.put('id', var.get('toID')(var.get('x'), var.get('y'), var.get('zoom')))
                    if var.get('tileHash').get(var.get('id')).neg():
                        var.get('tileArray').callprop('push', Js([var.get('x'), var.get('y'), var.get('zoom')]))
                finally:
                        (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
        finally:
                var.put('i', Js(2.0), '+')
PyJsHoisted_polygonCover_.func_name = 'polygonCover'
var.put('polygonCover', PyJsHoisted_polygonCover_)
@Js
def PyJsHoisted_tilesForEveryGeometry_(geometryTable, this, arguments, var=var):
    var = Scope({'this':this, 'geometryTable':geometryTable, 'arguments':arguments}, var)
    var.registers(['tileList', 'geometryTable'])
    var.put('tileList', var.get('Array').create())
    @Js
    def PyJs_anonymous_13_(element, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'element':element}, var)
        var.registers(['element'])
        var.put('tileList', var.get('tileList').callprop('concat', var.get('tilesForEveryZoom')(var.get('element'))))
    PyJs_anonymous_13_._set_name('anonymous')
    var.get('geometryTable').callprop('forEach', PyJs_anonymous_13_)
    return var.get('tileList')
PyJsHoisted_tilesForEveryGeometry_.func_name = 'tilesForEveryGeometry'
var.put('tilesForEveryGeometry', PyJsHoisted_tilesForEveryGeometry_)
@Js
def PyJsHoisted_appendHashTiles_(hash, tiles, this, arguments, var=var):
    var = Scope({'this':this, 'tiles':tiles, 'hash':hash, 'arguments':arguments}, var)
    var.registers(['keys', 'tiles', 'i', 'hash'])
    var.put('keys', var.get('Object').callprop('keys', var.get('hash')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('keys').get('length')):
        try:
            var.get('tiles').callprop('push', var.get('fromID')((+var.get('keys').get(var.get('i')))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_appendHashTiles_.func_name = 'appendHashTiles'
var.put('appendHashTiles', PyJsHoisted_appendHashTiles_)
@Js
def PyJsHoisted_getTiles_(geom, limits, this, arguments, var=var):
    var = Scope({'geom':geom, 'this':this, 'arguments':arguments, 'limits':limits}, var)
    var.registers(['geom', 'tile', 'tiles', 'maxZoom', 't', 'i', 'coords', 'limits', 'tileHash', 'len'])
    var.put('coords', var.get('geom').get('coordinates'))
    var.put('maxZoom', var.get('limits').get('max_zoom'))
    PyJs_Object_0_ = Js({})
    var.put('tileHash', PyJs_Object_0_)
    var.put('tiles', Js([]))
    if PyJsStrictEq(var.get('geom').get('type'),Js('Point')):
        return Js([var.get('pointToTile')(var.get('coords').get('0'), var.get('coords').get('1'), var.get('maxZoom'))])
    else:
        if PyJsStrictEq(var.get('geom').get('type'),Js('MultiPoint')):
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('coords').get('length')):
                try:
                    var.put('tile', var.get('pointToTile')(var.get('coords').get(var.get('i')).get('0'), var.get('coords').get(var.get('i')).get('1'), var.get('maxZoom')))
                    var.get('tileHash').put(var.get('toID')(var.get('tile').get('0'), var.get('tile').get('1'), var.get('tile').get('2')), var.get('true'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        else:
            if PyJsStrictEq(var.get('geom').get('type'),Js('LineString')):
                var.get('lineCover')(var.get('tileHash'), var.get('coords'), var.get('maxZoom'))
            else:
                if PyJsStrictEq(var.get('geom').get('type'),Js('MultiLineString')):
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('coords').get('length')):
                        try:
                            var.get('lineCover')(var.get('tileHash'), var.get('coords').get(var.get('i')), var.get('maxZoom'))
                        finally:
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                else:
                    if PyJsStrictEq(var.get('geom').get('type'),Js('Polygon')):
                        var.get('polygonCover')(var.get('tileHash'), var.get('tiles'), var.get('coords'), var.get('maxZoom'))
                    else:
                        if PyJsStrictEq(var.get('geom').get('type'),Js('MultiPolygon')):
                            #for JS loop
                            var.put('i', Js(0.0))
                            while (var.get('i')<var.get('coords').get('length')):
                                try:
                                    var.get('polygonCover')(var.get('tileHash'), var.get('tiles'), var.get('coords').get(var.get('i')), var.get('maxZoom'))
                                finally:
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        else:
                            PyJsTempException = JsToPyException(var.get('Error').create(Js('Geometry type not implemented')))
                            raise PyJsTempException
    if PyJsStrictNeq(var.get('limits').get('min_zoom'),var.get('maxZoom')):
        var.put('len', var.get('tiles').get('length'))
        var.get('appendHashTiles')(var.get('tileHash'), var.get('tiles'))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('len')):
            try:
                var.put('t', var.get('tiles').get(var.get('i')))
                var.get('tileHash').put(var.get('toID')(var.get('t').get('0'), var.get('t').get('1'), var.get('t').get('2')), var.get('true'))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return var.get('mergeTiles')(var.get('tileHash'), var.get('tiles'), var.get('limits'))
    var.get('appendHashTiles')(var.get('tileHash'), var.get('tiles'))
    return var.get('tiles')
PyJsHoisted_getTiles_.func_name = 'getTiles'
var.put('getTiles', PyJsHoisted_getTiles_)
@Js
def PyJsHoisted_mergeTiles_(tileHash, tiles, limits, this, arguments, var=var):
    var = Scope({'this':this, 'tiles':tiles, 'limits':limits, 'tileHash':tileHash, 'arguments':arguments}, var)
    var.registers(['parentTileHash', 'id2', 'id4', 'tiles', 'parentTiles', 'mergedTiles', 't', 'i', 'id3', 'parentTile', 'limits', 'z', 'tileHash'])
    var.put('mergedTiles', Js([]))
    #for JS loop
    var.put('z', var.get('limits').get('max_zoom'))
    while (var.get('z')>var.get('limits').get('min_zoom')):
        try:
            PyJs_Object_1_ = Js({})
            var.put('parentTileHash', PyJs_Object_1_)
            var.put('parentTiles', Js([]))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('tiles').get('length')):
                try:
                    var.put('t', var.get('tiles').get(var.get('i')))
                    if (PyJsStrictEq((var.get('t').get('0')%Js(2.0)),Js(0.0)) and PyJsStrictEq((var.get('t').get('1')%Js(2.0)),Js(0.0))):
                        var.put('id2', var.get('toID')((var.get('t').get('0')+Js(1.0)), var.get('t').get('1'), var.get('z')))
                        var.put('id3', var.get('toID')(var.get('t').get('0'), (var.get('t').get('1')+Js(1.0)), var.get('z')))
                        var.put('id4', var.get('toID')((var.get('t').get('0')+Js(1.0)), (var.get('t').get('1')+Js(1.0)), var.get('z')))
                        if ((var.get('tileHash').get(var.get('id2')) and var.get('tileHash').get(var.get('id3'))) and var.get('tileHash').get(var.get('id4'))):
                            var.get('tileHash').put(var.get('toID')(var.get('t').get('0'), var.get('t').get('1'), var.get('t').get('2')), Js(False))
                            var.get('tileHash').put(var.get('id2'), Js(False))
                            var.get('tileHash').put(var.get('id3'), Js(False))
                            var.get('tileHash').put(var.get('id4'), Js(False))
                            var.put('parentTile', Js([(var.get('t').get('0')/Js(2.0)), (var.get('t').get('1')/Js(2.0)), (var.get('z')-Js(1.0))]))
                            if PyJsStrictEq((var.get('z')-Js(1.0)),var.get('limits').get('min_zoom')):
                                var.get('mergedTiles').callprop('push', var.get('parentTile'))
                            else:
                                var.get('parentTileHash').put(var.get('toID')((var.get('t').get('0')/Js(2.0)), (var.get('t').get('1')/Js(2.0)), (var.get('z')-Js(1.0))), var.get('true'))
                                var.get('parentTiles').callprop('push', var.get('parentTile'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('tiles').get('length')):
                try:
                    var.put('t', var.get('tiles').get(var.get('i')))
                    if var.get('tileHash').get(var.get('toID')(var.get('t').get('0'), var.get('t').get('1'), var.get('t').get('2'))):
                        var.get('mergedTiles').callprop('push', var.get('t'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('tileHash', var.get('parentTileHash'))
            var.put('tiles', var.get('parentTiles'))
        finally:
                (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
    return var.get('mergedTiles')
PyJsHoisted_mergeTiles_.func_name = 'mergeTiles'
var.put('mergeTiles', PyJsHoisted_mergeTiles_)
@Js
def PyJsHoisted_getGeometryFromJSON_(geojsonObject, this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments, 'geojsonObject':geojsonObject}, var)
    var.registers(['geometryTable', 'geojsonObject'])
    var.put('geometryTable', var.get('Array').create())
    @Js
    def PyJs_anonymous_12_(element, this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments, 'element':element}, var)
        var.registers(['element'])
        var.get('geometryTable').callprop('push', var.get('element').get('geometry'))
    PyJs_anonymous_12_._set_name('anonymous')
    var.get('geojsonObject').get('features').callprop('forEach', PyJs_anonymous_12_)
    return var.get('geometryTable')
PyJsHoisted_getGeometryFromJSON_.func_name = 'getGeometryFromJSON'
var.put('getGeometryFromJSON', PyJsHoisted_getGeometryFromJSON_)
@Js
def PyJsHoisted_compareTiles_(a, b, this, arguments, var=var):
    var = Scope({'b':b, 'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    return ((var.get('a').get('1')-var.get('b').get('1')) or (var.get('a').get('0')-var.get('b').get('0')))
PyJsHoisted_compareTiles_.func_name = 'compareTiles'
var.put('compareTiles', PyJsHoisted_compareTiles_)
@Js
def PyJsHoisted_lineCover_(tileHash, coords, maxZoom, ring, this, arguments, var=var):
    var = Scope({'coords':coords, 'maxZoom':maxZoom, 'this':this, 'arguments':arguments, 'ring':ring, 'tileHash':tileHash}, var)
    var.registers(['y0', 'sx', 'coords', 'tMaxY', 'tdx', 'y', 'prevX', 'maxZoom', 'x1', 'ring', 'sy', 'tMaxX', 'tileHash', 'stop', 'i', 'tdy', 'x', 'y1', 'dy', 'prevY', 'x0', 'start', 'dx'])
    pass
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('coords').get('length')-Js(1.0))):
        try:
            var.put('start', var.get('pointToTileFraction')(var.get('coords').get(var.get('i')).get('0'), var.get('coords').get(var.get('i')).get('1'), var.get('maxZoom')))
            var.put('stop', var.get('pointToTileFraction')(var.get('coords').get((var.get('i')+Js(1.0))).get('0'), var.get('coords').get((var.get('i')+Js(1.0))).get('1'), var.get('maxZoom')))
            var.put('x0', var.get('start').get('0'))
            var.put('y0', var.get('start').get('1'))
            var.put('x1', var.get('stop').get('0'))
            var.put('y1', var.get('stop').get('1'))
            var.put('dx', (var.get('x1')-var.get('x0')))
            var.put('dy', (var.get('y1')-var.get('y0')))
            if (PyJsStrictEq(var.get('dy'),Js(0.0)) and PyJsStrictEq(var.get('dx'),Js(0.0))):
                continue
            var.put('sx', (Js(1.0) if (var.get('dx')>Js(0.0)) else (-Js(1.0))))
            var.put('sy', (Js(1.0) if (var.get('dy')>Js(0.0)) else (-Js(1.0))))
            var.put('x', var.get('Math').callprop('floor', var.get('x0')))
            var.put('y', var.get('Math').callprop('floor', var.get('y0')))
            var.put('tMaxX', (var.get('Infinity') if PyJsStrictEq(var.get('dx'),Js(0.0)) else var.get('Math').callprop('abs', ((((Js(1.0) if (var.get('dx')>Js(0.0)) else Js(0.0))+var.get('x'))-var.get('x0'))/var.get('dx')))))
            var.put('tMaxY', (var.get('Infinity') if PyJsStrictEq(var.get('dy'),Js(0.0)) else var.get('Math').callprop('abs', ((((Js(1.0) if (var.get('dy')>Js(0.0)) else Js(0.0))+var.get('y'))-var.get('y0'))/var.get('dy')))))
            var.put('tdx', var.get('Math').callprop('abs', (var.get('sx')/var.get('dx'))))
            var.put('tdy', var.get('Math').callprop('abs', (var.get('sy')/var.get('dy'))))
            if (PyJsStrictNeq(var.get('x'),var.get('prevX')) or PyJsStrictNeq(var.get('y'),var.get('prevY'))):
                var.get('tileHash').put(var.get('toID')(var.get('x'), var.get('y'), var.get('maxZoom')), var.get('true'))
                if (var.get('ring') and PyJsStrictNeq(var.get('y'),var.get('prevY'))):
                    var.get('ring').callprop('push', Js([var.get('x'), var.get('y')]))
                var.put('prevX', var.get('x'))
                var.put('prevY', var.get('y'))
            while ((var.get('tMaxX')<Js(1.0)) or (var.get('tMaxY')<Js(1.0))):
                if (var.get('tMaxX')<var.get('tMaxY')):
                    var.put('tMaxX', var.get('tdx'), '+')
                    var.put('x', var.get('sx'), '+')
                else:
                    var.put('tMaxY', var.get('tdy'), '+')
                    var.put('y', var.get('sy'), '+')
                var.get('tileHash').put(var.get('toID')(var.get('x'), var.get('y'), var.get('maxZoom')), var.get('true'))
                if (var.get('ring') and PyJsStrictNeq(var.get('y'),var.get('prevY'))):
                    var.get('ring').callprop('push', Js([var.get('x'), var.get('y')]))
                var.put('prevX', var.get('x'))
                var.put('prevY', var.get('y'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if (var.get('ring') and PyJsStrictEq(var.get('y'),var.get('ring').get('0').get('1'))):
        var.get('ring').callprop('pop')
PyJsHoisted_lineCover_.func_name = 'lineCover'
var.put('lineCover', PyJsHoisted_lineCover_)
@Js
def PyJsHoisted_fromID_(id, this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments, 'id':id}, var)
    var.registers(['dim', 'xy', 'x', 'y', 'z', 'id'])
    var.put('z', (var.get('id')%Js(32.0)))
    var.put('dim', (Js(2.0)*(Js(1.0)<<var.get('z'))))
    var.put('xy', ((var.get('id')-var.get('z'))/Js(32.0)))
    var.put('x', (var.get('xy')%var.get('dim')))
    var.put('y', (((var.get('xy')-var.get('x'))/var.get('dim'))%var.get('dim')))
    return Js([var.get('x'), var.get('y'), var.get('z')])
PyJsHoisted_fromID_.func_name = 'fromID'
var.put('fromID', PyJsHoisted_fromID_)
var.put('d2r', (var.get('Math').get('PI')/Js(180.0)))
var.put('r2d', (Js(180.0)/var.get('Math').get('PI')))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
PyJs_Object_4_ = Js({})
PyJs_Object_5_ = Js({'type':Js('Polygon'),'coordinates':Js([Js([Js([Js(1.4350461959838867), Js(43.586919026109854)]), Js([Js(1.4366769790649414), Js(43.586919026109854)]), Js([Js(1.4366769790649414), Js(43.587882648457935)]), Js([Js(1.4350461959838867), Js(43.587882648457935)]), Js([Js(1.4350461959838867), Js(43.586919026109854)])])])})
PyJs_Object_3_ = Js({'type':Js('Feature'),'properties':PyJs_Object_4_,'geometry':PyJs_Object_5_})
PyJs_Object_7_ = Js({})
PyJs_Object_8_ = Js({'type':Js('Polygon'),'coordinates':Js([Js([Js([Js(1.4335012435913086), Js(43.583437423271334)]), Js([Js(1.4347457885742188), Js(43.583437423271334)]), Js([Js(1.4347457885742188), Js(43.58430784285869)]), Js([Js(1.4335012435913086), Js(43.58430784285869)]), Js([Js(1.4335012435913086), Js(43.583437423271334)])])])})
PyJs_Object_6_ = Js({'type':Js('Feature'),'properties':PyJs_Object_7_,'geometry':PyJs_Object_8_})
PyJs_Object_10_ = Js({})
PyJs_Object_11_ = Js({'type':Js('Polygon'),'coordinates':Js([Js([Js([Js(1.4316987991333008), Js(43.57983126519667)]), Js([Js(1.4335012435913086), Js(43.57945820203314)]), Js([Js(1.4332437515258787), Js(43.58088826494042)]), Js([Js(1.4316987991333008), Js(43.57983126519667)])])])})
PyJs_Object_9_ = Js({'type':Js('Feature'),'properties':PyJs_Object_10_,'geometry':PyJs_Object_11_})
PyJs_Object_2_ = Js({'type':Js('FeatureCollection'),'features':Js([PyJs_Object_3_, PyJs_Object_6_, PyJs_Object_9_])})
var.put('geometryPolygonMultiple', PyJs_Object_2_)
pass
pass
pass
pass
pass


# Add lib to the module scope
cascade = var.to_python()