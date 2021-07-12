# python3

def merge(left, right):
    p1, p2, count = 0, 0, 0
    final = list()
    while p1 < len(left) and p2< len(right):
        if left[p1] <= right[p2]:
            final.append(left[p1])
            p1 += 1
        else:
            final.append(right[p2])
            count += len(left) - p1
            p2 += 1

    final += left[p1:]
    final += right[p2:]
        
    return final, count

def mergesort(arr):
    global tot_count
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    sorted_arr, temp = merge(left, right)
    tot_count += temp

    return sorted_arr

tot_count = 0
n = int(input())
seq = [int(p1) for p1 in input().split()]
mergesort(seq)
print(tot_count)


