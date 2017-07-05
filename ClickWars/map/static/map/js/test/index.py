__all__ = ['index']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['mergeTiles', 'polygonCover', 'toID', 'fromID', 'lineCover', 'getTiles', 'compareTiles', 'tileToFeature', 'tilebelt', 'appendHashTiles'])
@Js
def PyJsHoisted_mergeTiles_(tileHash, tiles, limits, this, arguments, var=var):
    var = Scope({'tileHash':tileHash, 'arguments':arguments, 'this':this, 'tiles':tiles, 'limits':limits}, var)
    var.registers(['t', 'id2', 'id3', 'id4', 'parentTileHash', 'parentTiles', 'z', 'tileHash', 'i', 'mergedTiles', 'parentTile', 'tiles', 'limits'])
    var.put('mergedTiles', Js([]))
    #for JS loop
    var.put('z', var.get('limits').get('max_zoom'))
    while (var.get('z')>var.get('limits').get('min_zoom')):
        try:
            PyJs_Object_6_ = Js({})
            var.put('parentTileHash', PyJs_Object_6_)
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
def PyJsHoisted_polygonCover_(tileHash, tileArray, geom, zoom, this, arguments, var=var):
    var = Scope({'tileHash':tileHash, 'geom':geom, 'zoom':zoom, 'arguments':arguments, 'this':this, 'tileArray':tileArray}, var)
    var.registers(['m', 'intersections', 'x', 'y', 'zoom', 'tileArray', 'id', 'tileHash', 'j', 'ring', 'i', 'len', 'geom', 'k'])
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
def PyJsHoisted_getTiles_(geom, limits, this, arguments, var=var):
    var = Scope({'geom':geom, 'arguments':arguments, 'this':this, 'limits':limits}, var)
    var.registers(['t', 'geom', 'limits', 'coords', 'tileHash', 'i', 'len', 'maxZoom', 'tiles', 'tile'])
    var.put('coords', var.get('geom').get('coordinates'))
    var.put('maxZoom', var.get('limits').get('max_zoom'))
    PyJs_Object_5_ = Js({})
    var.put('tileHash', PyJs_Object_5_)
    var.put('tiles', Js([]))
    if PyJsStrictEq(var.get('geom').get('type'),Js('Point')):
        return Js([var.get('tilebelt').callprop('pointToTile', var.get('coords').get('0'), var.get('coords').get('1'), var.get('maxZoom'))])
    else:
        if PyJsStrictEq(var.get('geom').get('type'),Js('MultiPoint')):
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('coords').get('length')):
                try:
                    var.put('tile', var.get('tilebelt').callprop('pointToTile', var.get('coords').get(var.get('i')).get('0'), var.get('coords').get(var.get('i')).get('1'), var.get('maxZoom')))
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
def PyJsHoisted_fromID_(id, this, arguments, var=var):
    var = Scope({'id':id, 'arguments':arguments, 'this':this}, var)
    var.registers(['xy', 'y', 'z', 'id', 'dim', 'x'])
    var.put('z', (var.get('id')%Js(32.0)))
    var.put('dim', (Js(2.0)*(Js(1.0)<<var.get('z'))))
    var.put('xy', ((var.get('id')-var.get('z'))/Js(32.0)))
    var.put('x', (var.get('xy')%var.get('dim')))
    var.put('y', (((var.get('xy')-var.get('x'))/var.get('dim'))%var.get('dim')))
    return Js([var.get('x'), var.get('y'), var.get('z')])
PyJsHoisted_fromID_.func_name = 'fromID'
var.put('fromID', PyJsHoisted_fromID_)
@Js
def PyJsHoisted_compareTiles_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'arguments':arguments, 'this':this}, var)
    var.registers(['a', 'b'])
    return ((var.get('a').get('1')-var.get('b').get('1')) or (var.get('a').get('0')-var.get('b').get('0')))
PyJsHoisted_compareTiles_.func_name = 'compareTiles'
var.put('compareTiles', PyJsHoisted_compareTiles_)
@Js
def PyJsHoisted_toID_(x, y, z, this, arguments, var=var):
    var = Scope({'x':x, 'y':y, 'arguments':arguments, 'this':this, 'z':z}, var)
    var.registers(['x', 'y', 'dim', 'z'])
    var.put('dim', (Js(2.0)*(Js(1.0)<<var.get('z'))))
    return ((((var.get('dim')*var.get('y'))+var.get('x'))*Js(32.0))+var.get('z'))
PyJsHoisted_toID_.func_name = 'toID'
var.put('toID', PyJsHoisted_toID_)
@Js
def PyJsHoisted_tileToFeature_(t, this, arguments, var=var):
    var = Scope({'t':t, 'arguments':arguments, 'this':this}, var)
    var.registers(['t'])
    PyJs_Object_3_ = Js({})
    PyJs_Object_2_ = Js({'type':Js('Feature'),'geometry':var.get('tilebelt').callprop('tileToGeoJSON', var.get('t')),'properties':PyJs_Object_3_})
    return PyJs_Object_2_
PyJsHoisted_tileToFeature_.func_name = 'tileToFeature'
var.put('tileToFeature', PyJsHoisted_tileToFeature_)
@Js
def PyJsHoisted_lineCover_(tileHash, coords, maxZoom, ring, this, arguments, var=var):
    var = Scope({'coords':coords, 'tileHash':tileHash, 'ring':ring, 'maxZoom':maxZoom, 'arguments':arguments, 'this':this}, var)
    var.registers(['prevX', 'coords', 'stop', 'i', 'maxZoom', 'tMaxY', 'dy', 'prevY', 'tMaxX', 'x', 'dx', 'tdy', 'tdx', 'y', 'start', 'y1', 'y0', 'sx', 'ring', 'x0', 'x1', 'tileHash', 'sy'])
    pass
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('coords').get('length')-Js(1.0))):
        try:
            var.put('start', var.get('tilebelt').callprop('pointToTileFraction', var.get('coords').get(var.get('i')).get('0'), var.get('coords').get(var.get('i')).get('1'), var.get('maxZoom')))
            var.put('stop', var.get('tilebelt').callprop('pointToTileFraction', var.get('coords').get((var.get('i')+Js(1.0))).get('0'), var.get('coords').get((var.get('i')+Js(1.0))).get('1'), var.get('maxZoom')))
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
def PyJsHoisted_appendHashTiles_(hash, tiles, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'hash':hash, 'tiles':tiles, 'this':this}, var)
    var.registers(['tiles', 'keys', 'hash', 'i'])
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
Js('use strict')
var.put('tilebelt', var.get('require')(Js('@mapbox/tilebelt')))
@Js
def PyJs_anonymous_0_(geom, limits, this, arguments, var=var):
    var = Scope({'geom':geom, 'arguments':arguments, 'this':this, 'limits':limits}, var)
    var.registers(['geom', 'limits'])
    PyJs_Object_1_ = Js({'type':Js('FeatureCollection'),'features':var.get('getTiles')(var.get('geom'), var.get('limits')).callprop('map', var.get('tileToFeature'))})
    return PyJs_Object_1_
PyJs_anonymous_0_._set_name('anonymous')
var.get('exports').put('geojson', PyJs_anonymous_0_)
pass
var.get('exports').put('tiles', var.get('getTiles'))
@Js
def PyJs_anonymous_4_(geom, limits, this, arguments, var=var):
    var = Scope({'geom':geom, 'arguments':arguments, 'this':this, 'limits':limits}, var)
    var.registers(['geom', 'limits'])
    return var.get('getTiles')(var.get('geom'), var.get('limits')).callprop('map', var.get('tilebelt').get('tileToQuadkey'))
PyJs_anonymous_4_._set_name('anonymous')
var.get('exports').put('indexes', PyJs_anonymous_4_)
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
index = var.to_python()