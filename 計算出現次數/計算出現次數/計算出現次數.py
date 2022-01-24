import collections
I=[0,1,1,1,2,3,7,23]
# Version 1
d=dict()
for i in I:
    d[i]=d.get(i,0)+1
    #print(d[i])
print(d)

# Version 2
x=set(I)
y=[I.count(i) for i in x]
for a,b in zip(x,y):
    print(a,b)

# Version 3
counter=collections.Counter(I)
for k,v in counter.items():
    print(k,v)