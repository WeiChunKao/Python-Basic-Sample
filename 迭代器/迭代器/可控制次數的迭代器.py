class BoundedRepeater:
    def __init__(self,value,max_repeates):
        self.value=value
        self.max_repeates=max_repeates
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count>=self.max_repeates:
            raise StopIteration
        self.count+=1
        return self.value
repeater=BoundedRepeater('Hello',3)
for item in repeater:
    print(item)