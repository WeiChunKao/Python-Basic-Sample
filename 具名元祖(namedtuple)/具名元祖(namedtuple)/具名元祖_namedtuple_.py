from collections import namedtuple
Car=namedtuple('Car',['color','mileage'])
mycar=Car('red',3812)
print(mycar.color)
print(mycar[0])
print(tuple(mycar))
print(*mycar)