# python3
import random
import time
def quicksort3(arr, l, r):
    
    if l + 1 >= r:
        return

    # select random pivot
    m = random.randint(l, r-1)

    arr[l], arr[m] = arr[m], arr[l]

    # partition procedure
    part1, part2 = partition3(arr, l, r)

    quicksort3(arr, l, part1)
    quicksort3(arr, part2+1, r)

def partition3(arr, l, r):
    part2 = l
    for i in range(l+1, r):
        if arr[i] <= arr[l]:
            arr[part2+1], arr[i] = arr[i], arr[part2+1]
            part2 += 1

    arr[l], arr[part2] = arr[part2], arr[l]

    part1 = l
    for i in range(l, part2):
        if arr[i] < arr[part2]:
            arr[i], arr[part1] = arr[part1], arr[i]
            part1 += 1
    return part1, part2

def create_array(size):
    return [random.choice(list(range(10))) for _ in range(size)]



t1 = time.time()
seq = create_array(100000)
quicksort3(seq, 0, 100000)
t2 = time.time()
print('Time taken:', t2-t1)

    

