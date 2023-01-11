#!/usr/bin/python3
BaseGeometry = _import_('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e._class.name_, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e._class.name_, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e._class.name_, e))
