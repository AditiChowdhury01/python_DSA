def bubble(arr):
    n = len(arr)
    for i in range(len(arr)):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        #if not swapped:
         #   break

arr = [3,45,-23,7,40,34]
bubble(arr)
print("the sorted array is:")
print(arr)