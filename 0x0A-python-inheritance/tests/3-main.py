#!/usr/bin/python3
is_kind_of_class = _import_('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int._name_))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float._name_))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object._name_))
