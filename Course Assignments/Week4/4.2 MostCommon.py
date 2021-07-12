# python3
n = int(input())
seq = [int(i) for i in input().split()]


seq.sort()
count=0
last_seen=0
x =len(seq)//2
answered=False
for num in seq:
    if last_seen == num:
        count+=1
        if count>x:
            answered=True
            break
    else:
        count=1
        last_seen=num

print(answered)

