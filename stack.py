class stack:
    def __init__(self):
        self.values=[]
    def push(self,item):
        return self.values.append(item)
    def pop(self):
        if not (self.isEmpty()):
            return self.values.pop()
        else:
            print("stack underflow")
            return None
    def isEmpty(self):
        return len(self.values)==0
    def size(self):
        return len(self.values)
    def front(self):
        if not(self.isEmpty()):
            return self.values[-1]
        else:
            print("stack empty")
            return None
        
s = stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.values)

s.pop()
s.pop()
s.pop()
s.pop()
print(s.values)

print(s.isEmpty())
print(s.size())
print(s.front())