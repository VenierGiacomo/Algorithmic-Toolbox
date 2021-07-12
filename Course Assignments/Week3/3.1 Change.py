# #Python3
n = int(input())
n_of_coins = 0
for i in [10, 5, 1]:
    if n>=i:
        q = n//i
        n_of_coins += q
        n = n%i
        if n==0:
            print(n_of_coins)
            quit()


