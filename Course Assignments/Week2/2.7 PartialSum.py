# Python3

m, n = [int(i) for i in input().split()]

if n<=1:
    print(n)  
    quit()


#It is known that sum of n Fibonacci numbers = F(n+2) -1
#pisano period of 10 is 60
smaller_than_sequence_n = (n+2)%60 
smaller_than_sequence_m = (m+1)%60 

def fibo(n):
    a,b = 0, 1
    for _ in range(2,n+1):
        c = a+b
        c = c%10 #we consider only the last digit of the fibonacci number
        b, a = c, b
        
    if c!=0:
        return(c-1)
    else:
        print(9)

last_dig__m = fibo(smaller_than_sequence_m)
last_dig__n = fibo(smaller_than_sequence_n)
if last_dig__m > last_dig__n:
    print(10+last_dig__n - last_dig__m)
else:
    print( last_dig__n - last_dig__n)
