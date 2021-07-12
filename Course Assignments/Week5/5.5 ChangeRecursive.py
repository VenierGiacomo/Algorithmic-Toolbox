import sys

def get_change(price):
    coins = [0]*(price+1)
    #change with coins 1, 3, 4
    for ind in range(1,price+1):
    	if ind <3:
    		coins[ind] = ind
    	elif ind <5 :
    		coins[ind] = 1
    	else:
    		coins[ind] = min(coins[ind-1],coins[ind-3],coins[ind-4])+1
    return coins[price]		



    return 

if __name__ == '__main__':
    price = int(sys.stdin.read())
    print(get_change(price))