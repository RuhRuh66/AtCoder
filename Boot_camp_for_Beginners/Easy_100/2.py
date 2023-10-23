N = int(input())
place = list(map(int, input().split()))

import statistics

s = round(statistics.mean(place))

ans = 0
for i in place:
    ans += pow(i-s, 2)
    
print(ans)