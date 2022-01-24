from collections import namedtuple
import json
Car=namedtuple('Car','color mileage')
class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color=='red':
            return '#ff0000'
        else:
            return '#000000'
c=MyCarWithMethods('red',1234)
print(c.hexcolor())
print(c._asdict())
print(json.dumps(c._asdict()))
print(Car._make(['red',999]))
