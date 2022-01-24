from types import SimpleNamespace
car1= SimpleNamespace(color='red',mileage=3812.4,automatic=True)
print(car1)
#支援屬性項存取，實體是可變的
car1.mileage=12
car1.windshield='broken'
del car1.automatic
print(car1)