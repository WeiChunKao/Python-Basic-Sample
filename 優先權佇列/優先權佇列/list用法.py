q=[]
q.append((2,'code'))
q.append((1,'eat'))
q.append((3,'sleep'))
#每當插入新元素，都要重新排序
#或使用biset.insort()
q.sort(reverse=True)
while q:
    next_item=q.pop()
    print(next_item)
