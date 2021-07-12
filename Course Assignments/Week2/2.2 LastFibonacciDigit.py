# Python3

n = int(input())
if n<=1:
    print(n)
def lastdigitfibo(n):
    #for memory usage and ease of computation we only store the last digit of  fiboacci numbers
    n1, n2 = 0, 1
    for _ in range(n-1):
        res = n1 + n2
        res = res % 10
        n1 =  n2
        n2 = res
    print(res)

lastdigitfibo(n)