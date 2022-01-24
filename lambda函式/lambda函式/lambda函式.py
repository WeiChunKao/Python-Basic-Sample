add = lambda x,y:x+y
print(add(3,5))

tuples=[(1,'d'),(2,'b'),(4,'a'),(3,'c')]
print(sorted(tuples,key=lambda x:x[1]))

print(sorted(range(-5,6),key=lambda x:x*x))

def make_adder(n):
    return lambda x:x+n
plus_3=make_adder(3)
print(plus_3(4))
plus_5=make_adder(5)
print(plus_5(4))