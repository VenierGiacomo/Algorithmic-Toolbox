# python3
n = int(input())
remaining_candies = n
if remaining_candies == 1:
    print(1)
    print(1)
    quit()
prizes = []
for num in range(n):
    remaining_candies-=num
    prizes.append(num)
    if num>=remaining_candies:
        prizes[-1]+=remaining_candies
        break

print(len(prizes))
print(' '.join([str(prize) for prize in prizes]))