__all__ = ['nodemapbrowser']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['anonymous','jsonToTiles'])
@Js
def PyJs_anonymous_1_(require, module, exports, this, arguments, var=var):
    var = Scope({'this':this, 'module':module, 'exports':exports, 'require':require, 'arguments':arguments}, var)
    var.registers(['module', 'exports', 'require', 'jsonToTiles'])
    @Js
    def PyJsHoisted_jsonToTiles_(polygonjson, this, arguments, var=var):
        var = Scope({'polygonjson':polygonjson, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'y', 'cover', 'x', 'polygonjson', 'limits', 'z', 'tilesRaw'])
        var.put('polyjsonstring', var.get('JSON').callprop('stringify', var.get('polygonjson')))
        var.put('polyjsonparse', var.get('JSON').callprop('parse', var.get('polyjsonstring')))
        var.put('cover', var.get('require')(Js('@mapbox/tile-cover')))
        PyJs_Object_2_ = Js({'min_zoom':Js(2.0),'max_zoom':Js(16.0)})
        var.put('limits', PyJs_Object_2_)
        var.put('tilesRaw', var.get('cover').callprop('tiles', var.get('polyjsonparse'), var.get('limits')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('tilesRaw').get('length')):
            try:
                var.put('x', var.get('tilesRaw').get(var.get('i')).get('0'))
                var.put('y', var.get('tilesRaw').get(var.get('i')).get('1'))
                var.put('z', var.get('tilesRaw').get(var.get('i')).get('2'))
                var.put('tileUrl', ((((((Js('http://{s}.tile.openstreetmap.org/')+var.get('z'))+Js('/'))+var.get('x'))+Js('/'))+var.get('y'))+Js('.png')))
                var.put('tileUrl', var.get('tileUrl').callprop('replace', Js('{s}.'), Js('')))
                var.get('console').callprop('log', ((var.get('i')+Js(' : '))+var.get('tileUrl')))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    PyJsHoisted_jsonToTiles_.func_name = 'jsonToTiles'
    var.put('jsonToTiles', PyJsHoisted_jsonToTiles_)
    pass
PyJs_anonymous_1_._set_name('anonymous')
PyJs_Object_3_ = Js({'@mapbox/tile-cover':Js(2.0)})
@Js
def PyJs_anonymous_4_(require, module, exports, this, arguments, var=var):
    var = Scope({'this':this, 'module':module, 'exports':exports, 'require':require, 'arguments':arguments}, var)
    var.registers(['module', 'polygonCover', 'lineCover', 'exports', 'toID', 'tileToFeature', 'fromID', 'require', 'compareTiles', 'mergeTiles', 'appendHashTiles', 'getTiles', 'tilebelt'])
    @Js
    def PyJsHoisted_lineCover_(tileHash, coords, maxZoom, ring, this, arguments, var=var):
        var = Scope({'maxZoom':maxZoom, 'coords':coords, 'arguments':arguments, 'this':this, 'tileHash':tileHash, 'ring':ring}, var)
        var.registers(['tMaxY', 'tileHash', 'x0', 'sx', 'prevX', 'tdy', 'prevY', 'maxZoom', 'coords', 'y', 'x', 'tdx', 'y0', 'dy', 'ring', 'y1', 'stop', 'dx', 'i', 'tMaxX', 'x1', 'start', 'sy'])
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
    def PyJsHoisted_compareTiles_(a, b, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'b':b, 'arguments':arguments}, var)
        var.registers(['a', 'b'])
        return ((var.get('a').get('1')-var.get('b').get('1')) or (var.get('a').get('0')-var.get('b').get('0')))
    PyJsHoisted_compareTiles_.func_name = 'compareTiles'
    var.put('compareTiles', PyJsHoisted_compareTiles_)
    @Js
    def PyJsHoisted_polygonCover_(tileHash, tileArray, geom, zoom, this, arguments, var=var):
        var = Scope({'tileArray':tileArray, 'zoom':zoom, 'geom':geom, 'this':this, 'arguments':arguments, 'tileHash':tileHash}, var)
        var.registers(['intersections', 'tileArray', 'i', 'y', 'zoom', 'm', 'x', 'tileHash', 'ring', 'len', 'k', 'j', 'geom', 'id'])
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
    def PyJsHoisted_mergeTiles_(tileHash, tiles, limits, this, arguments, var=var):
        var = Scope({'this':this, 'tiles':tiles, 'tileHash':tileHash, 'limits':limits, 'arguments':arguments}, var)
        var.registers(['tiles', 'z', 'i', 'id2', 'parentTile', 'tileHash', 'parentTileHash', 'id4', 'mergedTiles', 'id3', 'parentTiles', 'limits', 't'])
        var.put('mergedTiles', Js([]))
        #for JS loop
        var.put('z', var.get('limits').get('max_zoom'))
        while (var.get('z')>var.get('limits').get('min_zoom')):
            try:
                PyJs_Object_11_ = Js({})
                var.put('parentTileHash', PyJs_Object_11_)
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
    def PyJsHoisted_fromID_(id, this, arguments, var=var):
        var = Scope({'this':this, 'id':id, 'arguments':arguments}, var)
        var.registers(['y', 'x', 'dim', 'id', 'xy', 'z'])
        var.put('z', (var.get('id')%Js(32.0)))
        var.put('dim', (Js(2.0)*(Js(1.0)<<var.get('z'))))
        var.put('xy', ((var.get('id')-var.get('z'))/Js(32.0)))
        var.put('x', (var.get('xy')%var.get('dim')))
        var.put('y', (((var.get('xy')-var.get('x'))/var.get('dim'))%var.get('dim')))
        return Js([var.get('x'), var.get('y'), var.get('z')])
    PyJsHoisted_fromID_.func_name = 'fromID'
    var.put('fromID', PyJsHoisted_fromID_)
    @Js
    def PyJsHoisted_appendHashTiles_(hash, tiles, this, arguments, var=var):
        var = Scope({'hash':hash, 'tiles':tiles, 'this':this, 'arguments':arguments}, var)
        var.registers(['hash', 'tiles', 'i', 'keys'])
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
        var = Scope({'geom':geom, 'this':this, 'limits':limits, 'arguments':arguments}, var)
        var.registers(['maxZoom', 'tiles', 'i', 'coords', 'tileHash', 'len', 'tile', 'geom', 'limits', 't'])
        var.put('coords', var.get('geom').get('coordinates'))
        var.put('maxZoom', var.get('limits').get('max_zoom'))
        PyJs_Object_10_ = Js({})
        var.put('tileHash', PyJs_Object_10_)
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
    def PyJsHoisted_tileToFeature_(t, this, arguments, var=var):
        var = Scope({'this':this, 't':t, 'arguments':arguments}, var)
        var.registers(['t'])
        PyJs_Object_8_ = Js({})
        PyJs_Object_7_ = Js({'type':Js('Feature'),'geometry':var.get('tilebelt').callprop('tileToGeoJSON', var.get('t')),'properties':PyJs_Object_8_})
        return PyJs_Object_7_
    PyJsHoisted_tileToFeature_.func_name = 'tileToFeature'
    var.put('tileToFeature', PyJsHoisted_tileToFeature_)
    @Js
    def PyJsHoisted_toID_(x, y, z, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'z':z, 'y':y, 'arguments':arguments}, var)
        var.registers(['y', 'x', 'z', 'dim'])
        var.put('dim', (Js(2.0)*(Js(1.0)<<var.get('z'))))
        return ((((var.get('dim')*var.get('y'))+var.get('x'))*Js(32.0))+var.get('z'))
    PyJsHoisted_toID_.func_name = 'toID'
    var.put('toID', PyJsHoisted_toID_)
    Js('use strict')
    var.put('tilebelt', var.get('require')(Js('@mapbox/tilebelt')))
    @Js
    def PyJs_anonymous_5_(geom, limits, this, arguments, var=var):
        var = Scope({'geom':geom, 'this':this, 'limits':limits, 'arguments':arguments}, var)
        var.registers(['geom', 'limits'])
        PyJs_Object_6_ = Js({'type':Js('FeatureCollection'),'features':var.get('getTiles')(var.get('geom'), var.get('limits')).callprop('map', var.get('tileToFeature'))})
        return PyJs_Object_6_
    PyJs_anonymous_5_._set_name('anonymous')
    var.get('exports').put('geojson', PyJs_anonymous_5_)
    pass
    var.get('exports').put('tiles', var.get('getTiles'))
    @Js
    def PyJs_anonymous_9_(geom, limits, this, arguments, var=var):
        var = Scope({'geom':geom, 'this':this, 'limits':limits, 'arguments':arguments}, var)
        var.registers(['geom', 'limits'])
        return var.get('getTiles')(var.get('geom'), var.get('limits')).callprop('map', var.get('tilebelt').get('tileToQuadkey'))
    PyJs_anonymous_9_._set_name('anonymous')
    var.get('exports').put('indexes', PyJs_anonymous_9_)
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
PyJs_anonymous_4_._set_name('anonymous')
PyJs_Object_12_ = Js({'@mapbox/tilebelt':Js(3.0)})
@Js
def PyJs_anonymous_13_(require, module, exports, this, arguments, var=var):
    var = Scope({'this':this, 'module':module, 'exports':exports, 'require':require, 'arguments':arguments}, var)
    var.registers(['module', 'pointToTileFraction', 'exports', 'getParent', 'pointToTile', 'r2d', 'getSiblings', 'tile2lat', 'hasTile', 'tileToQuadkey', 'quadkeyToTile', 'tileToGeoJSON', 'tileToBBOX', 'd2r', 'hasSiblings', 'bboxToTile', 'getBboxZoom', 'require', 'tile2lon', 'getChildren', 'tilesEqual'])
    @Js
    def PyJsHoisted_pointToTileFraction_(lon, lat, z, this, arguments, var=var):
        var = Scope({'lon':lon, 'this':this, 'lat':lat, 'z':z, 'arguments':arguments}, var)
        var.registers(['z', 'y', 'z2', 'x', 'lon', 'lat', 'sin'])
        var.put('sin', var.get('Math').callprop('sin', (var.get('lat')*var.get('d2r'))))
        var.put('z2', var.get('Math').callprop('pow', Js(2.0), var.get('z')))
        var.put('x', (var.get('z2')*((var.get('lon')/Js(360.0))+Js(0.5))))
        var.put('y', (var.get('z2')*(Js(0.5)-((Js(0.25)*var.get('Math').callprop('log', ((Js(1.0)+var.get('sin'))/(Js(1.0)-var.get('sin')))))/var.get('Math').get('PI')))))
        return Js([var.get('x'), var.get('y'), var.get('z')])
    PyJsHoisted_pointToTileFraction_.func_name = 'pointToTileFraction'
    var.put('pointToTileFraction', PyJsHoisted_pointToTileFraction_)
    @Js
    def PyJsHoisted_getParent_(tile, this, arguments, var=var):
        var = Scope({'this':this, 'tile':tile, 'arguments':arguments}, var)
        var.registers(['tile'])
        if (PyJsStrictEq((var.get('tile').get('0')%Js(2.0)),Js(0.0)) and PyJsStrictEq((var.get('tile').get('1')%Js(2.0)),Js(0.0))):
            return Js([(var.get('tile').get('0')/Js(2.0)), (var.get('tile').get('1')/Js(2.0)), (var.get('tile').get('2')-Js(1.0))])
        if (PyJsStrictEq((var.get('tile').get('0')%Js(2.0)),Js(0.0)) and PyJsStrictEq((var.get('tile').get('1').neg()%Js(2.0)),Js(0.0))):
            return Js([(var.get('tile').get('0')/Js(2.0)), ((var.get('tile').get('1')-Js(1.0))/Js(2.0)), (var.get('tile').get('2')-Js(1.0))])
        if (PyJsStrictEq((var.get('tile').get('0').neg()%Js(2.0)),Js(0.0)) and PyJsStrictEq((var.get('tile').get('1')%Js(2.0)),Js(0.0))):
            return Js([((var.get('tile').get('0')-Js(1.0))/Js(2.0)), (var.get('tile').get('1')/Js(2.0)), (var.get('tile').get('2')-Js(1.0))])
        return Js([((var.get('tile').get('0')-Js(1.0))/Js(2.0)), ((var.get('tile').get('1')-Js(1.0))/Js(2.0)), (var.get('tile').get('2')-Js(1.0))])
    PyJsHoisted_getParent_.func_name = 'getParent'
    var.put('getParent', PyJsHoisted_getParent_)
    @Js
    def PyJsHoisted_pointToTile_(lon, lat, z, this, arguments, var=var):
        var = Scope({'lon':lon, 'this':this, 'lat':lat, 'z':z, 'arguments':arguments}, var)
        var.registers(['lon', 'z', 'lat', 'tile'])
        var.put('tile', var.get('pointToTileFraction')(var.get('lon'), var.get('lat'), var.get('z')))
        var.get('tile').put('0', var.get('Math').callprop('floor', var.get('tile').get('0')))
        var.get('tile').put('1', var.get('Math').callprop('floor', var.get('tile').get('1')))
        return var.get('tile')
    PyJsHoisted_pointToTile_.func_name = 'pointToTile'
    var.put('pointToTile', PyJsHoisted_pointToTile_)
    @Js
    def PyJsHoisted_hasTile_(tiles, tile, this, arguments, var=var):
        var = Scope({'tiles':tiles, 'this':this, 'tile':tile, 'arguments':arguments}, var)
        var.registers(['tiles', 'i', 'tile'])
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('tiles').get('length')):
            try:
                if var.get('tilesEqual')(var.get('tiles').get(var.get('i')), var.get('tile')):
                    return var.get('true')
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return Js(False)
    PyJsHoisted_hasTile_.func_name = 'hasTile'
    var.put('hasTile', PyJsHoisted_hasTile_)
    @Js
    def PyJsHoisted_tileToGeoJSON_(tile, this, arguments, var=var):
        var = Scope({'this':this, 'tile':tile, 'arguments':arguments}, var)
        var.registers(['bbox', 'poly', 'tile'])
        var.put('bbox', var.get('tileToBBOX')(var.get('tile')))
        PyJs_Object_14_ = Js({'type':Js('Polygon'),'coordinates':Js([Js([Js([var.get('bbox').get('0'), var.get('bbox').get('1')]), Js([var.get('bbox').get('0'), var.get('bbox').get('3')]), Js([var.get('bbox').get('2'), var.get('bbox').get('3')]), Js([var.get('bbox').get('2'), var.get('bbox').get('1')]), Js([var.get('bbox').get('0'), var.get('bbox').get('1')])])])})
        var.put('poly', PyJs_Object_14_)
        return var.get('poly')
    PyJsHoisted_tileToGeoJSON_.func_name = 'tileToGeoJSON'
    var.put('tileToGeoJSON', PyJsHoisted_tileToGeoJSON_)
    @Js
    def PyJsHoisted_tile2lat_(y, z, this, arguments, var=var):
        var = Scope({'this':this, 'z':z, 'y':y, 'arguments':arguments}, var)
        var.registers(['z', 'n', 'y'])
        var.put('n', (var.get('Math').get('PI')-(((Js(2.0)*var.get('Math').get('PI'))*var.get('y'))/var.get('Math').callprop('pow', Js(2.0), var.get('z')))))
        return (var.get('r2d')*var.get('Math').callprop('atan', (Js(0.5)*(var.get('Math').callprop('exp', var.get('n'))-var.get('Math').callprop('exp', (-var.get('n')))))))
    PyJsHoisted_tile2lat_.func_name = 'tile2lat'
    var.put('tile2lat', PyJsHoisted_tile2lat_)
    @Js
    def PyJsHoisted_getSiblings_(tile, this, arguments, var=var):
        var = Scope({'this':this, 'tile':tile, 'arguments':arguments}, var)
        var.registers(['tile'])
        return var.get('getChildren')(var.get('getParent')(var.get('tile')))
    PyJsHoisted_getSiblings_.func_name = 'getSiblings'
    var.put('getSiblings', PyJsHoisted_getSiblings_)
    @Js
    def PyJsHoisted_quadkeyToTile_(quadkey, this, arguments, var=var):
        var = Scope({'this':this, 'quadkey':quadkey, 'arguments':arguments}, var)
        var.registers(['i', 'quadkey', 'y', 'x', 'q', 'mask', 'z'])
        var.put('x', Js(0.0))
        var.put('y', Js(0.0))
        var.put('z', var.get('quadkey').get('length'))
        #for JS loop
        var.put('i', var.get('z'))
        while (var.get('i')>Js(0.0)):
            try:
                var.put('mask', (Js(1.0)<<(var.get('i')-Js(1.0))))
                var.put('q', (+var.get('quadkey').get((var.get('z')-var.get('i')))))
                if PyJsStrictEq(var.get('q'),Js(1.0)):
                    var.put('x', var.get('mask'), '|')
                if PyJsStrictEq(var.get('q'),Js(2.0)):
                    var.put('y', var.get('mask'), '|')
                if PyJsStrictEq(var.get('q'),Js(3.0)):
                    var.put('x', var.get('mask'), '|')
                    var.put('y', var.get('mask'), '|')
            finally:
                    (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
        return Js([var.get('x'), var.get('y'), var.get('z')])
    PyJsHoisted_quadkeyToTile_.func_name = 'quadkeyToTile'
    var.put('quadkeyToTile', PyJsHoisted_quadkeyToTile_)
    @Js
    def PyJsHoisted_tileToBBOX_(tile, this, arguments, var=var):
        var = Scope({'this':this, 'tile':tile, 'arguments':arguments}, var)
        var.registers(['w', 'tile', 'n', 's', 'e'])
        var.put('e', var.get('tile2lon')((var.get('tile').get('0')+Js(1.0)), var.get('tile').get('2')))
        var.put('w', var.get('tile2lon')(var.get('tile').get('0'), var.get('tile').get('2')))
        var.put('s', var.get('tile2lat')((var.get('tile').get('1')+Js(1.0)), var.get('tile').get('2')))
        var.put('n', var.get('tile2lat')(var.get('tile').get('1'), var.get('tile').get('2')))
        return Js([var.get('w'), var.get('s'), var.get('e'), var.get('n')])
    PyJsHoisted_tileToBBOX_.func_name = 'tileToBBOX'
    var.put('tileToBBOX', PyJsHoisted_tileToBBOX_)
    @Js
    def PyJsHoisted_hasSiblings_(tile, tiles, this, arguments, var=var):
        var = Scope({'tiles':tiles, 'this':this, 'tile':tile, 'arguments':arguments}, var)
        var.registers(['tiles', 'siblings', 'i', 'tile'])
        var.put('siblings', var.get('getSiblings')(var.get('tile')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('siblings').get('length')):
            try:
                if var.get('hasTile')(var.get('tiles'), var.get('siblings').get(var.get('i'))).neg():
                    return Js(False)
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return var.get('true')
    PyJsHoisted_hasSiblings_.func_name = 'hasSiblings'
    var.put('hasSiblings', PyJsHoisted_hasSiblings_)
    @Js
    def PyJsHoisted_getBboxZoom_(bbox, this, arguments, var=var):
        var = Scope({'bbox':bbox, 'this':this, 'arguments':arguments}, var)
        var.registers(['bbox', 'mask', 'z', 'MAX_ZOOM'])
        var.put('MAX_ZOOM', Js(28.0))
        #for JS loop
        var.put('z', Js(0.0))
        while (var.get('z')<var.get('MAX_ZOOM')):
            try:
                var.put('mask', (Js(1.0)<<(Js(32.0)-(var.get('z')+Js(1.0)))))
                if (PyJsStrictNeq((var.get('bbox').get('0')&var.get('mask')),(var.get('bbox').get('2')&var.get('mask'))) or PyJsStrictNeq((var.get('bbox').get('1')&var.get('mask')),(var.get('bbox').get('3')&var.get('mask')))):
                    return var.get('z')
            finally:
                    (var.put('z',Js(var.get('z').to_number())+Js(1))-Js(1))
        return var.get('MAX_ZOOM')
    PyJsHoisted_getBboxZoom_.func_name = 'getBboxZoom'
    var.put('getBboxZoom', PyJsHoisted_getBboxZoom_)
    @Js
    def PyJsHoisted_tileToQuadkey_(tile, this, arguments, var=var):
        var = Scope({'this':this, 'tile':tile, 'arguments':arguments}, var)
        var.registers(['b', 'tile', 'mask', 'index', 'z'])
        var.put('index', Js(''))
        #for JS loop
        var.put('z', var.get('tile').get('2'))
        while (var.get('z')>Js(0.0)):
            try:
                var.put('b', Js(0.0))
                var.put('mask', (Js(1.0)<<(var.get('z')-Js(1.0))))
                if PyJsStrictNeq((var.get('tile').get('0')&var.get('mask')),Js(0.0)):
                    (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
                if PyJsStrictNeq((var.get('tile').get('1')&var.get('mask')),Js(0.0)):
                    var.put('b', Js(2.0), '+')
                var.put('index', var.get('b').callprop('toString'), '+')
            finally:
                    (var.put('z',Js(var.get('z').to_number())-Js(1))+Js(1))
        return var.get('index')
    PyJsHoisted_tileToQuadkey_.func_name = 'tileToQuadkey'
    var.put('tileToQuadkey', PyJsHoisted_tileToQuadkey_)
    @Js
    def PyJsHoisted_tile2lon_(x, z, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'z':z, 'arguments':arguments}, var)
        var.registers(['x', 'z'])
        return (((var.get('x')/var.get('Math').callprop('pow', Js(2.0), var.get('z')))*Js(360.0))-Js(180.0))
    PyJsHoisted_tile2lon_.func_name = 'tile2lon'
    var.put('tile2lon', PyJsHoisted_tile2lon_)
    @Js
    def PyJsHoisted_getChildren_(tile, this, arguments, var=var):
        var = Scope({'this':this, 'tile':tile, 'arguments':arguments}, var)
        var.registers(['tile'])
        return Js([Js([(var.get('tile').get('0')*Js(2.0)), (var.get('tile').get('1')*Js(2.0)), (var.get('tile').get('2')+Js(1.0))]), Js([((var.get('tile').get('0')*Js(2.0))+Js(1.0)), (var.get('tile').get('1')*Js(2.0)), (var.get('tile').get('2')+Js(1.0))]), Js([((var.get('tile').get('0')*Js(2.0))+Js(1.0)), ((var.get('tile').get('1')*Js(2.0))+Js(1.0)), (var.get('tile').get('2')+Js(1.0))]), Js([(var.get('tile').get('0')*Js(2.0)), ((var.get('tile').get('1')*Js(2.0))+Js(1.0)), (var.get('tile').get('2')+Js(1.0))])])
    PyJsHoisted_getChildren_.func_name = 'getChildren'
    var.put('getChildren', PyJsHoisted_getChildren_)
    @Js
    def PyJsHoisted_tilesEqual_(tile1, tile2, this, arguments, var=var):
        var = Scope({'arguments':arguments, 'tile2':tile2, 'this':this, 'tile1':tile1}, var)
        var.registers(['tile2', 'tile1'])
        return ((PyJsStrictEq(var.get('tile1').get('0'),var.get('tile2').get('0')) and PyJsStrictEq(var.get('tile1').get('1'),var.get('tile2').get('1'))) and PyJsStrictEq(var.get('tile1').get('2'),var.get('tile2').get('2')))
    PyJsHoisted_tilesEqual_.func_name = 'tilesEqual'
    var.put('tilesEqual', PyJsHoisted_tilesEqual_)
    @Js
    def PyJsHoisted_bboxToTile_(bboxCoords, this, arguments, var=var):
        var = Scope({'bboxCoords':bboxCoords, 'this':this, 'arguments':arguments}, var)
        var.registers(['max', 'y', 'x', 'bboxCoords', 'min', 'bbox', 'z'])
        var.put('min', var.get('pointToTile')(var.get('bboxCoords').get('0'), var.get('bboxCoords').get('1'), Js(32.0)))
        var.put('max', var.get('pointToTile')(var.get('bboxCoords').get('2'), var.get('bboxCoords').get('3'), Js(32.0)))
        var.put('bbox', Js([var.get('min').get('0'), var.get('min').get('1'), var.get('max').get('0'), var.get('max').get('1')]))
        var.put('z', var.get('getBboxZoom')(var.get('bbox')))
        if PyJsStrictEq(var.get('z'),Js(0.0)):
            return Js([Js(0.0), Js(0.0), Js(0.0)])
        var.put('x', PyJsBshift(var.get('bbox').get('0'),(Js(32.0)-var.get('z'))))
        var.put('y', PyJsBshift(var.get('bbox').get('1'),(Js(32.0)-var.get('z'))))
        return Js([var.get('x'), var.get('y'), var.get('z')])
    PyJsHoisted_bboxToTile_.func_name = 'bboxToTile'
    var.put('bboxToTile', PyJsHoisted_bboxToTile_)
    Js('use strict')
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
    pass
    pass
    pass
    pass
    pass
    pass
    PyJs_Object_15_ = Js({'tileToGeoJSON':var.get('tileToGeoJSON'),'tileToBBOX':var.get('tileToBBOX'),'getChildren':var.get('getChildren'),'getParent':var.get('getParent'),'getSiblings':var.get('getSiblings'),'hasTile':var.get('hasTile'),'hasSiblings':var.get('hasSiblings'),'tilesEqual':var.get('tilesEqual'),'tileToQuadkey':var.get('tileToQuadkey'),'quadkeyToTile':var.get('quadkeyToTile'),'pointToTile':var.get('pointToTile'),'bboxToTile':var.get('bboxToTile'),'pointToTileFraction':var.get('pointToTileFraction')})
    var.get('module').put('exports', PyJs_Object_15_)
PyJs_anonymous_13_._set_name('anonymous')
PyJs_Object_16_ = Js({})
PyJs_Object_0_ = Js({'1':Js([PyJs_anonymous_1_, PyJs_Object_3_]),'2':Js([PyJs_anonymous_4_, PyJs_Object_12_]),'3':Js([PyJs_anonymous_13_, PyJs_Object_16_])})
PyJs_Object_17_ = Js({})
@Js
def PyJs_e_18_(t, n, r, this, arguments, var=var):
    var = Scope({'e':PyJs_e_18_, 'arguments':arguments, 'n':n, 'r':r, 'this':this, 't':t}, var)
    var.registers(['i', 'o', 's', 'r', 'n', 't'])
    @Js
    def PyJsHoisted_s_(o, u, this, arguments, var=var):
        var = Scope({'o':o, 'u':u, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'o', 'u', 'l', 'f'])
        if var.get('n').get(var.get('o')).neg():
            if var.get('t').get(var.get('o')).neg():
                var.put('a', ((var.get('require',throw=False).typeof()==Js('function')) and var.get('require')))
                if (var.get('u').neg() and var.get('a')):
                    return var.get('a')(var.get('o'), Js(0.0).neg())
                if var.get('i'):
                    return var.get('i')(var.get('o'), Js(0.0).neg())
                var.put('f', var.get('Error').create(((Js("Cannot find module '")+var.get('o'))+Js("'"))))
                PyJsTempException = JsToPyException(PyJsComma(var.get('f').put('code', Js('MODULE_NOT_FOUND')),var.get('f')))
                raise PyJsTempException
            PyJs_Object_20_ = Js({})
            PyJs_Object_19_ = Js({'exports':PyJs_Object_20_})
            var.put('l', var.get('n').put(var.get('o'), PyJs_Object_19_))
            @Js
            def PyJs_anonymous_21_(e, this, arguments, var=var):
                var = Scope({'arguments':arguments, 'this':this, 'e':e}, var)
                var.registers(['n', 'e'])
                var.put('n', var.get('t').get(var.get('o')).get('1').get(var.get('e')))
                return var.get('s')((var.get('n') if var.get('n') else var.get('e')))
            PyJs_anonymous_21_._set_name('anonymous')
            var.get('t').get(var.get('o')).get('0').callprop('call', var.get('l').get('exports'), PyJs_anonymous_21_, var.get('l'), var.get('l').get('exports'), var.get('e'), var.get('t'), var.get('n'), var.get('r'))
        return var.get('n').get(var.get('o')).get('exports')
    PyJsHoisted_s_.func_name = 's'
    var.put('s', PyJsHoisted_s_)
    pass
    var.put('i', ((var.get('require',throw=False).typeof()==Js('function')) and var.get('require')))
    #for JS loop
    var.put('o', Js(0.0))
    while (var.get('o')<var.get('r').get('length')):
        try:
            var.get('s')(var.get('r').get(var.get('o')))
        finally:
                (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
    return var.get('s')
PyJs_e_18_._set_name('e')
PyJs_e_18_(PyJs_Object_0_, PyJs_Object_17_, Js([Js(1.0)]))
pass


# Add lib to the module scope
nodemapbrowser = var.to_python()
