def integers():
    for i in range(1,9):
        yield i
chain=integers()
print(list(chain))