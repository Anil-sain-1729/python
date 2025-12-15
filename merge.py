def merge(arr):
    n = len(arr)

    if(n>1):
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0

        while i<len(left) and j<len(right):
            if(left[i]<right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i<len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j<len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [54,25,35,65,85,75,7]
print(arr)
merge(arr)
print(arr)