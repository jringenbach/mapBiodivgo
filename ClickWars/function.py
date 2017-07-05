__all__ = ['function']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['somme'])
@Js
def PyJsHoisted_somme_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'arguments':arguments, 'this':this, 'b':b}, var)
    var.registers(['a', 'b'])
    var.get('console').callprop('log', (var.get('a')+var.get('b')))
PyJsHoisted_somme_.func_name = 'somme'
var.put('somme', PyJsHoisted_somme_)
pass
pass


# Add lib to the module scope
function = var.to_python()