class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

#for inserting at the beggining og linked list
head =  node1
new_node = Node(50)
new_node.next= head
head = new_node

#traversing the linked list
current = head
while current is not None:
    print(current.data,end="->")
    current = current.next
print("none")