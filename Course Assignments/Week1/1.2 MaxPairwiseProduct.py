#Naive approach
def max_prod_naive(arr):
    product = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            product = max(product,arr[i]*arr[j])
    return product
#Fast approach
def max_prod_fast(arr):
    p1 = max(arr)
    arr.remove(p1)
    p2 = max(arr)
    return p1*p2
#Fast approach

def max_prod_fast2(arr):
    if len(arr)<2:
        return None
    max1=arr[1] if arr[0]>=arr[1] else arr[0]
    max2=arr[0] if arr[0]>=arr[1] else arr[1]
    for x in range(2,len(arr)):
        if arr[x]>max1:
            if arr[x]>max2:
                max2 = arr[x]
            else:
                max1 = arr[x]
    return max1 * max2


