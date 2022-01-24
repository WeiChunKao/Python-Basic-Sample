def myfunc(a,b):
    return a+b
funcs=[myfunc]
print(funcs[0](2,3))
def dispatch_dict(operator,x,y):
   return{
        'add':lambda:x+y,
        'sub':lambda:x-y,
        'mul':lambda:x*y,
        'div':lambda:x/y
    }.get(operator,lambda:None)()