from typing import NamedTuple
class Car (NamedTuple):
    color:str
    mileage:float
    automatic:bool
car1= Car('red',3812.4,True)
print(car1)
print(car1.mileage)
