#找不到key時，回傳預設值
from collections import defaultdict
dd= defaultdict(list)
#存取的key不在，defaultdict會建立它
#並以預設工廠函式初始化
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')
print(dd['dogs'])
print(dd)