import array
arr= array.array('f',(1.0,1.5,2.0,2.5))
print(arr[1])
print(arr)

#陣列是可變的
arr[1]=23.0
print(arr)

del arr[1]
print(arr)

arr.append(42.0)
print(arr)
#陣列元素必須是同一種型別