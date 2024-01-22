N, M = map(int, input().split())
from collections import defaultdict

cost = defaultdict(int)

for i in range(N):
    A, B = map(int, input().split())
    cost[A] += B
    
s = sorted(cost.items())

count = 0
total_cost = 0

for price, num in s:
    if count + num <= M:
        total_cost += price*num
        count += num
    else:
        total_cost += (M-count) * price
        break
    
print(total_cost)


