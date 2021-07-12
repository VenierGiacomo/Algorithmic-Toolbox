# Python3

n1, n2 = [int(i) for i in input().split()]

def euclid_gcd(n1, n2):
    if n2 == 0:
        return n1
    c = n1%n2
    return euclid_gcd(n2, c)

big= n1 if n1>n2 else n2
small = n2 if n1>n2 else n1

gcd = euclid_gcd(big, small)

print(n1*n2//gcd)