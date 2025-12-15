def bubbl(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [64,25,45,85,35,1]
print(arr)
bubbl(arr)
print(arr)