arr= bytearray((0,1,2,3))
print(arr[1])
print(arr)
#bytearray是可變的
arr[1]=23
print(arr)
print(arr[1])
#bytearray可變長度
del arr[1]
print(arr)
arr.append(42)
print(arr)

#bytearray 只能放進位元組
