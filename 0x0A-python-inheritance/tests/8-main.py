#!/usr/bin/python3
Rectangle = _import_('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e._class.name_, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e._class.name_, e))
