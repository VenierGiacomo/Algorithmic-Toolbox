# Python3
n = int(input())

if n<=1:
    print(n)  
    quit()

def fibo(n):
    n1, n2 = 0, 1
    for _ in range(n-1):
        res = n1 + n2
        n1 =  n2
        n2 = res
    print(res)

fibo(n)
