__all__ = ['indexbelt']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['tileToQuadkey', 'getChildren', 'hasTile', 'quadkeyToTile', 'tileToBBOX', 'tile2lat', 'pointToTileFraction', 'tile2lon', 'r2d', 'getSiblings', 'bboxToTile', 'getParent', 'hasSiblings', 'pointToTile', 'tileToGeoJSON', 'getBboxZoom', 'tilesEqual', 'd2r'])
@Js
def PyJsHoisted_tileToQuadkey_(tile, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'tile':tile}, var)
    var.registers(['mask', 'b', 'tile', 'z', 'index'])
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
def PyJsHoisted_getChildren_(tile, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'tile':tile}, var)
    var.registers(['tile'])
    return Js([Js([(var.get('tile').get('0')*Js(2.0)), (var.get('tile').get('1')*Js(2.0)), (var.get('tile').get('2')+Js(1.0))]), Js([((var.get('tile').get('0')*Js(2.0))+Js(1.0)), (var.get('tile').get('1')*Js(2.0)), (var.get('tile').get('2')+Js(1.0))]), Js([((var.get('tile').get('0')*Js(2.0))+Js(1.0)), ((var.get('tile').get('1')*Js(2.0))+Js(1.0)), (var.get('tile').get('2')+Js(1.0))]), Js([(var.get('tile').get('0')*Js(2.0)), ((var.get('tile').get('1')*Js(2.0))+Js(1.0)), (var.get('tile').get('2')+Js(1.0))])])
PyJsHoisted_getChildren_.func_name = 'getChildren'
var.put('getChildren', PyJsHoisted_getChildren_)
@Js
def PyJsHoisted_hasTile_(tiles, tile, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'tiles':tiles, 'tile':tile}, var)
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
def PyJsHoisted_getBboxZoom_(bbox, this, arguments, var=var):
    var = Scope({'bbox':bbox, 'arguments':arguments, 'this':this}, var)
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
def PyJsHoisted_tileToBBOX_(tile, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'tile':tile}, var)
    var.registers(['e', 's', 'tile', 'n', 'w'])
    var.put('e', var.get('tile2lon')((var.get('tile').get('0')+Js(1.0)), var.get('tile').get('2')))
    var.put('w', var.get('tile2lon')(var.get('tile').get('0'), var.get('tile').get('2')))
    var.put('s', var.get('tile2lat')((var.get('tile').get('1')+Js(1.0)), var.get('tile').get('2')))
    var.put('n', var.get('tile2lat')(var.get('tile').get('1'), var.get('tile').get('2')))
    return Js([var.get('w'), var.get('s'), var.get('e'), var.get('n')])
PyJsHoisted_tileToBBOX_.func_name = 'tileToBBOX'
var.put('tileToBBOX', PyJsHoisted_tileToBBOX_)
@Js
def PyJsHoisted_quadkeyToTile_(quadkey, this, arguments, var=var):
    var = Scope({'quadkey':quadkey, 'arguments':arguments, 'this':this}, var)
    var.registers(['y', 'quadkey', 'z', 'mask', 'i', 'x', 'q'])
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
def PyJsHoisted_tile2lon_(x, z, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this, 'z':z}, var)
    var.registers(['x', 'z'])
    return (((var.get('x')/var.get('Math').callprop('pow', Js(2.0), var.get('z')))*Js(360.0))-Js(180.0))
PyJsHoisted_tile2lon_.func_name = 'tile2lon'
var.put('tile2lon', PyJsHoisted_tile2lon_)
@Js
def PyJsHoisted_getSiblings_(tile, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'tile':tile}, var)
    var.registers(['tile'])
    return var.get('getChildren')(var.get('getParent')(var.get('tile')))
PyJsHoisted_getSiblings_.func_name = 'getSiblings'
var.put('getSiblings', PyJsHoisted_getSiblings_)
@Js
def PyJsHoisted_tilesEqual_(tile1, tile2, this, arguments, var=var):
    var = Scope({'tile2':tile2, 'arguments':arguments, 'this':this, 'tile1':tile1}, var)
    var.registers(['tile2', 'tile1'])
    return ((PyJsStrictEq(var.get('tile1').get('0'),var.get('tile2').get('0')) and PyJsStrictEq(var.get('tile1').get('1'),var.get('tile2').get('1'))) and PyJsStrictEq(var.get('tile1').get('2'),var.get('tile2').get('2')))
PyJsHoisted_tilesEqual_.func_name = 'tilesEqual'
var.put('tilesEqual', PyJsHoisted_tilesEqual_)
@Js
def PyJsHoisted_pointToTileFraction_(lon, lat, z, this, arguments, var=var):
    var = Scope({'lon':lon, 'lat':lat, 'arguments':arguments, 'this':this, 'z':z}, var)
    var.registers(['lat', 'y', 'lon', 'z', 'z2', 'sin', 'x'])
    var.put('sin', var.get('Math').callprop('sin', (var.get('lat')*var.get('d2r'))))
    var.put('z2', var.get('Math').callprop('pow', Js(2.0), var.get('z')))
    var.put('x', (var.get('z2')*((var.get('lon')/Js(360.0))+Js(0.5))))
    var.put('y', (var.get('z2')*(Js(0.5)-((Js(0.25)*var.get('Math').callprop('log', ((Js(1.0)+var.get('sin'))/(Js(1.0)-var.get('sin')))))/var.get('Math').get('PI')))))
    return Js([var.get('x'), var.get('y'), var.get('z')])
PyJsHoisted_pointToTileFraction_.func_name = 'pointToTileFraction'
var.put('pointToTileFraction', PyJsHoisted_pointToTileFraction_)
@Js
def PyJsHoisted_bboxToTile_(bboxCoords, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'bboxCoords':bboxCoords, 'this':this}, var)
    var.registers(['max', 'min', 'y', 'z', 'bboxCoords', 'x', 'bbox'])
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
@Js
def PyJsHoisted_hasSiblings_(tile, tiles, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'tiles':tiles, 'tile':tile}, var)
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
def PyJsHoisted_tile2lat_(y, z, this, arguments, var=var):
    var = Scope({'y':y, 'arguments':arguments, 'this':this, 'z':z}, var)
    var.registers(['y', 'n', 'z'])
    var.put('n', (var.get('Math').get('PI')-(((Js(2.0)*var.get('Math').get('PI'))*var.get('y'))/var.get('Math').callprop('pow', Js(2.0), var.get('z')))))
    return (var.get('r2d')*var.get('Math').callprop('atan', (Js(0.5)*(var.get('Math').callprop('exp', var.get('n'))-var.get('Math').callprop('exp', (-var.get('n')))))))
PyJsHoisted_tile2lat_.func_name = 'tile2lat'
var.put('tile2lat', PyJsHoisted_tile2lat_)
@Js
def PyJsHoisted_pointToTile_(lon, lat, z, this, arguments, var=var):
    var = Scope({'lon':lon, 'lat':lat, 'arguments':arguments, 'this':this, 'z':z}, var)
    var.registers(['lon', 'lat', 'z', 'tile'])
    var.put('tile', var.get('pointToTileFraction')(var.get('lon'), var.get('lat'), var.get('z')))
    var.get('tile').put('0', var.get('Math').callprop('floor', var.get('tile').get('0')))
    var.get('tile').put('1', var.get('Math').callprop('floor', var.get('tile').get('1')))
    return var.get('tile')
PyJsHoisted_pointToTile_.func_name = 'pointToTile'
var.put('pointToTile', PyJsHoisted_pointToTile_)
@Js
def PyJsHoisted_tileToGeoJSON_(tile, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'tile':tile}, var)
    var.registers(['bbox', 'poly', 'tile'])
    var.put('bbox', var.get('tileToBBOX')(var.get('tile')))
    PyJs_Object_0_ = Js({'type':Js('Polygon'),'coordinates':Js([Js([Js([var.get('bbox').get('0'), var.get('bbox').get('1')]), Js([var.get('bbox').get('0'), var.get('bbox').get('3')]), Js([var.get('bbox').get('2'), var.get('bbox').get('3')]), Js([var.get('bbox').get('2'), var.get('bbox').get('1')]), Js([var.get('bbox').get('0'), var.get('bbox').get('1')])])])})
    var.put('poly', PyJs_Object_0_)
    return var.get('poly')
PyJsHoisted_tileToGeoJSON_.func_name = 'tileToGeoJSON'
var.put('tileToGeoJSON', PyJsHoisted_tileToGeoJSON_)
@Js
def PyJsHoisted_getParent_(tile, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'tile':tile}, var)
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
PyJs_Object_1_ = Js({'tileToGeoJSON':var.get('tileToGeoJSON'),'tileToBBOX':var.get('tileToBBOX'),'getChildren':var.get('getChildren'),'getParent':var.get('getParent'),'getSiblings':var.get('getSiblings'),'hasTile':var.get('hasTile'),'hasSiblings':var.get('hasSiblings'),'tilesEqual':var.get('tilesEqual'),'tileToQuadkey':var.get('tileToQuadkey'),'quadkeyToTile':var.get('quadkeyToTile'),'pointToTile':var.get('pointToTile'),'bboxToTile':var.get('bboxToTile'),'pointToTileFraction':var.get('pointToTileFraction')})
var.get('module').put('exports', PyJs_Object_1_)
pass


# Add lib to the module scope
indexbelt = var.to_python()