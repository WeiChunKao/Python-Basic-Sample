from collections import namedtuple
from sys import getsizeof
p1= namedtuple('Point','x y z')(1,2,3)
p2=(1,2,3)
print(getsizeof(p1))
print(getsizeof(p2))
Car= namedtuple('Car','color mileage automatic')
car1=Car('red',3812.4,True)
print(car1)
#存取欄位
print(car1.mileage)
