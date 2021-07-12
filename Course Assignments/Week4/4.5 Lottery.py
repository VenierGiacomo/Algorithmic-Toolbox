# python3


# Inputs
master_list = list()
s, p = [int(i) for i in input().split()]

for i in range(s):
    start, end = [int(i) for i in input().split()]
    master_list.append((start,'start'))
    master_list.append((end,'end'))

points = input().split()
for i in points:
    master_list.append((int(i),'p'))

master_list.sort()

intersections = 0
hashmap = dict()
for i in master_list:
    if i[1] == 'start': intersections += 1
    elif i[1] == 'end': intersections -= 1
    else:
        hashmap[i[0]] = intersections

temp = ''
for i in points:
    temp += str(hashmap[int(i)]) + ' '
print(temp[:-1])
    





















