class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        current = self.head.next
        out=""
        while current:
            out = out+str(current.data)+"->"
            current = current.next
        return out[:-3]
    def getsize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if not(self.isEmpty()):
            return self.head.next.data
        else:
            print("stack underflow")
            return None
        
    def push(self,data):
        
        self.data = data