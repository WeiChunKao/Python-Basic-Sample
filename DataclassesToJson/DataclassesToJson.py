import dataclasses
import json
@dataclasses.dataclass()
class Employee(json.JSONEncoder):
    id:int
    name:str
#Version 1
class AdvancedJSONEncoder(json.JSONEncoder): 
      def default(self, obj):
        if isinstance(obj, Employee):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

e=Employee(1,"J")
print(json.dumps(e,cls=AdvancedJSONEncoder))

#Version 2
print(e.__dict__)
