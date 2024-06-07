def linear(array,target):
    for i in range(len(array)):
        if(array[i]==target):
            return i
    return -1
    

array = [34,23,65,12,13,0,5]
target = int(input("enter a number:"))
print(linear(array,target))