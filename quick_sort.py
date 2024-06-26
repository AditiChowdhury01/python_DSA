def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if(arr[j]<=pivot):
            i = i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]   

    return i+1

def quick_sort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

arr =[2,1,23,6,8,34,56,9]
size = len(arr)
quick_sort(arr,0,size-1)

print(arr)