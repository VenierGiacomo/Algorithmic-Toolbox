# python3
n = int(input())
digits = [int(i) for i in input().split()]

digits.sort(key = lambda x : str(x),reverse=True)

print(''.join([str(i) for i in digits]))
