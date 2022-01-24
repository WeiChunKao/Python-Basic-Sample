class Car:
    def __init__(self,color,mileage,automatic):
        self.color=color
        self.mileage=mileage
        self.automatic=automatic
car1=Car('red',3812.4,True)
print(car1.mileage)
#類別是可變的
car1.mileage=12
car1.windshield='broken'
print(car1.windshield)