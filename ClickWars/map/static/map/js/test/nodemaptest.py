__all__ = ['nodemaptest']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
import index
import indexbelt
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['jsonToTiles'])
@Js
def PyJsHoisted_jsonToTiles_(polygonjson, this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments, 'polygonjson':polygonjson}, var)
    var.registers(['x', 'limits', 'tilesRaw', 'cover', 'y', 'polygonjson', 'z', 'i'])
    var.put('polyjsonstring', var.get('JSON').callprop('stringify', var.get('polygonjson')))
    var.put('polyjsonparse', var.get('JSON').callprop('parse', var.get('polyjsonstring')))
    var.put('cover', var.get('require')(Js('@mapbox/tile-cover')))
    PyJs_Object_0_ = Js({'min_zoom':Js(2.0),'max_zoom':Js(16.0)})
    var.put('limits', PyJs_Object_0_)
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
pass


# Add lib to the module scope
nodemaptest = var.to_python()
