class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

new_node =Node(45)

head = node1
current = head
while current is not None and current.data!=40:
    current = current.next
new_node.next= current.next
current.next = new_node  

current = head
while current is not None:
    print(current.data,end="->")
    current = current.next
print("None")