__author__ = 'root'
from collections import  namedtuple
edmprimitivetype = namedtuple('name', 'type value')
__EDM_BINARY = edmprimitivetype('EDMBINARY', 'Edm.Binary')
__EDM_BOOLEAN = edmprimitivetype('EDMBOOLEAN', 'Edm.Boolean')
tupli = (__EDM_BOOLEAN.value,
         __EDM_BINARY.value,
         'Edm.String')
print(tupli.__len__())
if 'sasi' in tupli:
    print(True)
else:
    print(False)


# Point = namedtuple('Point', 'x y')
# pt1 = Point(1.0, 5.0)
# pt2 = Point(2.5, 1.5)
# print(pt1.x)