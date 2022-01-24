class Employee:
    def __init__(self,id):
        self.__id=id
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id=value
    def f1(self):
        print(f'id={self.__id}')
class Sales(Employee):
    pass
s=Sales(100)
s.f1()
s.id=500
s.f1()