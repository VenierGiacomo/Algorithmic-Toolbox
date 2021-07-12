# python3

import math

n = int(input())

# number of operations required for getting 0, 1, 2,.. , n
total_ops = [0, 0] + [math.inf]*(n-1)

for i in range(2, n+1):
    plus1, times2, times3 = [math.inf]*3

    
    if i%3 == 0: times3 = total_ops[i//3] + 1
    if i%2 == 0: times2 = total_ops[i//2] + 1
    plus1 = total_ops[i-1] + 1 
    min_ops = min(times3, times2, plus1  )
    total_ops[i] = min_ops

print(total_ops[n])

nums = [n]
while n!=1:
    if n%3 ==0 and total_ops[n]-1 == total_ops[n//3]:
        nums.append(n//3)
        n = n//3
    elif n%2 ==0 and total_ops[n]-1 == total_ops[n//2]:
        nums.append(n//2)
        n = n//2
    else:
        nums.append(n-1)
        n = n - 1

print(' '.join([str(num) for num in nums][::-1]))