squares=[x * x for x in range(10)]
print( squares)
even_squares=[x * x for x in range(10) if x%2 ==0]
print(even_squares)
print({x * x for x in range(-9,10)})
print({x: x * x for x in range(5)})