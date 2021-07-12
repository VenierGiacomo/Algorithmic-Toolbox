
#python3
#using Euclidean algo
#method to compute gcd
n1, n2 = [int(i) for i in input().split()]
    
def computeGCD(n1, n2): 
    while(n2):
        n1 , n2 =n2 , n1 % n2 
    return n1 
  
print (computeGCD(n1,n2)) 
