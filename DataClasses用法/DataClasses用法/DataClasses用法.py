import dataclasses
@dataclasses.dataclass #(repr=False)
class Employee:
    id:int
    name:str=dataclasses.field(repr=False)
e = Employee(1,"Wei")
I=[e]
print(I)
print(e)
