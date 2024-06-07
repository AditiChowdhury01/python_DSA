def binary_search(arr,target):
    low,high = 0,len(arr)-1
    while low<high:
        mid = low+high//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low = mid+1

        else:
            high= mid-1

    return-1
    
arr = [1,34,56,67,89]
target = int(input("enetr a number:"))
print(binary_search(arr,target))