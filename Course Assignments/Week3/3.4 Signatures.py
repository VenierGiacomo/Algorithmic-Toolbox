# # python3
n = int(input())
slots = []

for _ in range(n):
    start, end = [int(i) for i in input().split()]
    slots.append((start,end))
slots.sort(key = lambda x: x[0])
tot=0
curr_slot=slots[0]
coordinates=[]
for ind in range(1,len(slots)):
    if slots[ind][0] <=curr_slot[1]:
        curr_slot=min(curr_slot[1],slots[ind][1])
    else:
        coordinates.append(curr_slot[1])
        curr_slot = slots[ind]
print(coordinates)












