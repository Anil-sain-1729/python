def partiton(arr,low,high):
    pivot = arr[high]
    i = low-1

    for j in range(low,high):
        if(arr[j]<= pivot):
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick(arr,low,high):
    if(low<high):
        pi = partiton(arr,low,high)
        quick(arr,low,pi-1)
        quick(arr,pi+1,high)

arr = [14,12,51,45,25,35,65,95,85,75,121]
print(arr)
quick(arr,0,len(arr)-1)
print(arr)