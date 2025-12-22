def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1]= key

    return arr 

arr = [54,65,25,41,24,25]
print(arr)
insertion(arr)
print(arr)