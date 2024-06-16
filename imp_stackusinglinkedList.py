class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.size =0
    def push(self,data):
        if (self.head == None):
           self.head = Node(data)
           self.size+=1

        else:
           new_node = Node(data)
           new_node.next = self.head
           self.head = new_node
           self.size+=1
    def isEmpty(self):
        if (self.head == None):
            return True
        else:
            return False
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            poppedNode = self.head
            self.head = self.head.next
            self.size-=1
            #poppedNode.next= None
            return poppedNode.data
            
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
    #traversing the stack
    def display(self):
        current = self.head
        if self.isEmpty():
            print("stack underflow")
        else:
            while current!=None:
                print(current.data,end = "->")
                current = current.next
            print("none")
            print("the size of the linked list is:",self.size)


if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)

    s.display()

    s.pop()
    s.pop()
    print(s.pop())
    
    s.display()

    print(s.peek())
    print(s.isEmpty())

    s.display()




      