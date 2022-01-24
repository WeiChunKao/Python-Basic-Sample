class B1:
    def f1(self):
        print("B1::f1")
class B2:
    def f1(self):
        print("B2::f1")
class C1:
    def __new__(cls,parent_class):
        print("__new__")
        instance=object.__new__(parent_class)
        return instance
    def __init__(self):
        print("__init__")
c=C1(B1)
c.f1()
b=C1(B2)
b.f1()