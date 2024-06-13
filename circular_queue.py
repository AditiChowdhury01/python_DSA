class circular_queue:
    def __init__(self,k):
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1
    def enqueue(self,item):
        if ((self.tail+1)%self.k==self.head):
            print("the queue is empty")
        elif (self.head == -1):
            self.head = self.tail =0
            self.queue[self.tail]=item
        else:
            self.tail = (self.tail+1)%self.k
            self.queue[self.tail]=item

    def dequeue(self):
        if self.head == -1:
            print("the queue is empty")
        elif(self.head==self.tail):
            temp = self.queue[self.tail]
            self.head = self.tail = -1
            return temp
        else:
            temp = self.queue[self.tail]
            self.head = (self.head+1)%self.k
            return temp
        
    def printque(self):
        if self.head ==-1:
            print("queue is empty")
        elif self.tail>=self.head:
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end=" ")
            print()
        else:
            for i in range(self.head,self.k):
                print(self.queue[i],end=" ")
            
            for i in range(0,self.tail+1):
                print(self.queue[i],end=" ")
            print()

q = circular_queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.printque()

print(q.dequeue())

q.printque()
