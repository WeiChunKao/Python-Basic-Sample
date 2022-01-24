arr=['one','two','three']
print(arr[0])
print(arr)
#串列是可變動的
arr[1]='hello'
print(arr)

del arr[1]
print(arr)

#串列可以放進任何型別的資料
arr.append(23)
print(arr)