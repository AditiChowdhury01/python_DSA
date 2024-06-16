class priority_queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def isEmpty(self):
        return self.queue==0
    def dequeue(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if (self.queue[i]>self.queue[max]):
                    max = i
                    item = self.queue[max]
                    del self.queue[max]
                    return item
        except IndexError:
            print()
            return


q = priority_queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(q.dequeue())
print(q.isEmpty())