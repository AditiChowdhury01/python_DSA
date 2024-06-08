def selection(arr):
    n = len(arr)
    for i in range(0,n):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini = j
        arr[mini],arr[i] = arr[i],arr[mini]
        

arr = [23,34,12,25,2,1,-90,-34]
selection(arr)
print(arr)