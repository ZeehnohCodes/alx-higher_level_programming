#!/usr/bin/python3
BaseGeometry = _import_('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e._class.name_, e))
