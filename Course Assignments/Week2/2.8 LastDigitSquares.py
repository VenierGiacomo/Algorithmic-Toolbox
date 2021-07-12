# python3

n = int(input())
smaller_than_sequence_n = n%60
smaller_than_sequence_nplus = (n+1)%60

def fibo(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        c = a+b
        c = c% 10 # we condiserd onnly the last digit
        b, a = c, b
    return c

if smaller_than_sequence_n<=1:
    a = smaller_than_sequence_n
else:
    a = fibo(smaller_than_sequence_n)
if smaller_than_sequence_nplus<=1:
    b = smaller_than_sequence_nplus
else:
    b = fibo(smaller_than_sequence_nplus)

# the sum of n Fibonacci sqared is equal to the product of Fn and Fn+1
#then we print only the last digit
print((a*b)%10)