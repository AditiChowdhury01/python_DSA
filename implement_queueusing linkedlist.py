class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.rear = self.front = None
    def isEmpty(self):
        return self.front == None
    def Enqueue(self,data):
        current = Node(data)
        if self.rear==None:
            self.front = self.rear=current
            return
        
        self.rear.next = current
        self.rear = current
        
    def Dequeue(self):
        if self.isEmpty():            
            return
        current = self.front
        self.front = current.next
        if (self.front==None):
            self.rear = None

    


    def display(self):
        current = self.front
        if self.isEmpty():
            print ("queue underfow")
        else:
            while current !=None:
               print(current.data,end="<- ")
               current = current.next
            print("None")
            #print(self.rear)
if __name__=="__main__":
    q= Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.Enqueue(40)
    q.Enqueue(50)

    q.display()

    q.Dequeue()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()

    q.display()



            
            
