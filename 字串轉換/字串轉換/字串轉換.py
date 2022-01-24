class Car:
    def __init__(self, color, mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return f'a {self.color} car'
    def __repr__(self):
        return '__repr__ for car'
mycar=Car('red',123)
print(mycar)
print('{}'.format(mycar))
print(str(mycar))
print(repr(mycar))