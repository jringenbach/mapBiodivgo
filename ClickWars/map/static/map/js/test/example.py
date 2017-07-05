__all__ = ['example']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['someVariable', 'Rectangle', 'sayHello', '$nonPyName'])
@Js
def PyJsHoisted_Rectangle_(w, h, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'h':h, 'this':this, 'w':w}, var)
    var.registers(['w', 'h'])
    var.get(u"this").put('w', var.get('w'))
    var.get(u"this").put('h', var.get('h'))
PyJsHoisted_Rectangle_.func_name = 'Rectangle'
var.put('Rectangle', PyJsHoisted_Rectangle_)
@Js
def PyJsHoisted_sayHello_(name, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'name':name}, var)
    var.registers(['name'])
    var.get('console').callprop('log', ((Js('Hello, ')+var.get('name'))+Js('!')))
PyJsHoisted_sayHello_.func_name = 'sayHello'
var.put('sayHello', PyJsHoisted_sayHello_)
@Js
def PyJsHoistedNonPyName(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.get('console').callprop('log', Js('Non-Py names like $ can be used too!'))
PyJsHoistedNonPyName.func_name = '$nonPyName'
var.put('$nonPyName', PyJsHoistedNonPyName)
PyJs_Object_0_ = Js({'a':Js(1.0),'b':Js(2.0)})
var.put('someVariable', PyJs_Object_0_)
pass
pass
pass
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return (var.get(u"this").get('w')*var.get(u"this").get('h'))
PyJs_anonymous_2_._set_name('anonymous')
PyJs_Object_1_ = Js({'getArea':PyJs_anonymous_2_})
var.get('Rectangle').put('prototype', PyJs_Object_1_)
var.put('x', var.get('Rectangle').create(Js(10.0), Js(10.0)))


# Add lib to the module scope
example = var.to_python()