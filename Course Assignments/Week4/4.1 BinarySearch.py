# python3
nums = [int(i) for i in input().split()]
look_for = [int(i) for i in input().split()]
n = nums[0]
seq = nums[1:]

def binary_search(seq, look_up, r):
    l = 0
    while l<=r: 
        m = (l+r)//2
        if look_up > seq[m]:
            l = m + 1
        elif look_up < seq[m]:
            r = m - 1
        else:
            return m
    return -1

res = list()
for num in look_for[1:]:
    ans = binary_search(seq, num, n-1)
    res.append(ans)
    
print(' '.join([str(num) for num in res]))

