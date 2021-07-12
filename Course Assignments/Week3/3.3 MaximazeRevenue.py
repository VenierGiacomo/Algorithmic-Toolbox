# python3
n = int(input())
ads_earnings = [int(i) for i in input().split()]
spot_clicks = [int(i) for i in input().split()]
ads_earnings.sort()
spot_clicks.sort()
tot_revenues = sum([ads_earnings[i]*spot_clicks[i] for i in range(n)])
print(tot_revenues)