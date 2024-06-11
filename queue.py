class queues:
    def __init__(self):
        self.values=[]
    def enqueue(self,x):
        self.values.append(x)
    def dequeue(self):
        if not(self.isEmpty()):
            return self.values.pop(0)

            
        else:
            print("queue underflow")
            return None
        #self.values.pop(0)
        #front = self.values[0]
        #self.values = self.values[1:]
        #return front

    def isEmpty(self):
        return len(self.values)==0
    
    def front(self):
        if not(self.isEmpty()):
            return self.values[0]
        else:
            print("queue empty")
            return None
    def size(self):
        return len(self.values)
    
q = queues()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.values)

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
#q.dequeue()
print(q.values)


print(q.front())
print(q.isEmpty())
print(q.size())