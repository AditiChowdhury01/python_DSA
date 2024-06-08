def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1]= arr[j]
            j = j-1
        arr[j+1]=key

arr=[23,12,34,-45,23,6,9,7]
insertion_sort(arr)
print(arr)
