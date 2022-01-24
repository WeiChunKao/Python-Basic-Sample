#製作唯讀字典的包裹層
from types import MappingProxyType
writable={'one':1,'two':2}
read_only= MappingProxyType(writable)
#這個中介物件是唯讀的
print(read_only['one'])
#更新原來字典，也會反映到中介物件
writable['one']=42
print(read_only['one'])
print(read_only)