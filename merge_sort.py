def merge(left,right):
    new = []
    i,j=0,0

    while i <len(left) and j<len(right):
        if(left[i]<right[j]):
            new.append(left[i])
            i = i+1
        else:
            new.append(right[j])
            j = j+1

    new.extend(left[i:])
    new.extend(right[j:])
    return new

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right= merge_sort(right)

    return merge(left,right)

arr=[21,12,34,45,23,6,9,7]
sr=merge_sort(arr)
print(sr)