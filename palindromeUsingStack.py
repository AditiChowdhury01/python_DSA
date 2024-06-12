class Stack:
    def __init__(self):
        self.values = []
    def push(self,data):
        self.values.append(data)
    def pop(self):
        if not (self.isEmpty()):
            return self.values.pop()
        else:
            print("stack underflow")
            return None
    def isEmpty(self):
        return len(self.values) == 0
    
def is_palindrome(s):
    stk = Stack()
    for char in s:
        stk.push(char)
    for char in s:
        if char!=stk.pop():
            return False
    return True
    
#try:
target = input("enter a string:")
print(is_palindrome(target))
#except:
#print("cannot perform on integers")


    