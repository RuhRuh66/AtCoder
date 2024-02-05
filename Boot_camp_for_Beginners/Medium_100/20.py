from collections import defaultdict

d = defaultdict(int)

N = int(input())
for i in range(N):
    temp = int(input())
    d[temp] += 1
    
    
ans = [i for i, j in d.items() if j %2 == 1]

print(len(ans))