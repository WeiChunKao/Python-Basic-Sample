def print_vector(x,y,z):
    print('<%s, %s, %s>' % (x,y,z))
tuple_vec=(1,0,1)
list_vec=[1,0,1]
print_vector(tuple_vec[0],tuple_vec[1],tuple_vec[2])
print_vector(*tuple_vec)
genexpr=(x * x for x in range(3))
print_vector(*genexpr)
dict_vec={'y':0,'z':1,'x':1}
print_vector(**dict_vec)