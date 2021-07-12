# Python3
n, tot_capacity = [int(i) for i in input().split()]
lst = []

if tot_capacity == 0:
    print(0)
    quit()

for _ in range(n):
    value, quantity = [int(i) for i in input().split()]
    if value == 0:
        continue
    lst.append((value, quantity))

lst.sort(key = lambda x: x[0]/x[1], reverse = True)

total_value = 0

for value,capacity in lst:
    if tot_capacity==0:
        print(total_value)
        quit()
    amt = min(capacity, tot_capacity)
    total_value += amt*(value/capacity)
    tot_capacity -= amt

print(total_value)

