arr = [ 4,5,3,4,-2,-3,5,1,0,-1,-3,2]
a = list(set(arr))
sume = 0
for i in range(len(a)):
    sume += a[i]
print(sume)