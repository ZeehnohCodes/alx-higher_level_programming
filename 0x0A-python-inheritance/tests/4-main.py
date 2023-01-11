#!/usr/bin/python3
inherits_from = _import_('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int._name_))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool._name_))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object._name_))
