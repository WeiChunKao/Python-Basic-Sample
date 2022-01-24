#把多個字典當作一個映射結構進行搜尋
from collections import ChainMap
dict1={'one':1,'two':2}
dict2={'three':3,'four':4}
chain = ChainMap(dict1,dict2)
print(chain)
#ChainMap會從左到右，逐一搜尋
#每個群集，直到找到key(或者失敗、找不到)
print(chain['three'])
#print(chain['missing'])