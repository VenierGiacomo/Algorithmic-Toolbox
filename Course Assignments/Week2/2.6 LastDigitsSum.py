# Python3

n = int(input())

if n<=1:
    print(n)  
    quit()


#It is known that sum of n Fibonacci numbers = F(n+2) -1
#pisano period of 10 is 60
smaller_than_sequence = (n+2)%60 

if smaller_than_sequence==1:
    print(0)
    quit()
elif smaller_than_sequence==0:
    print(9)
    quit()
def fibo(n):
    a,b = 0, 1
    for _ in range(2,n+1):
        c = a+b
        c = c%10 #we consider only the last digit of the fibonacci number
        b, a = c, b
        
    if c!=0:
        print(c-1)
    else:
        print(9)
fibo(smaller_than_sequence)
