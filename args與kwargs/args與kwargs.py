def foo(required,*args,**kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

print(foo('Hello'))
print(foo('hello',1,2,3))
print(foo('Hello',1,2,3,key1='value',key2=999))
