N = int(input())

from itertools import combinations

plots = []
for i in range(N):
    temp = list(map(int, input().split()))
    plots.append(temp)

s = combinations(plots, 3)


for i in s:
    if (i[1][1]-i[0][1])*(i[2][0]-i[0][0]) == (i[1][0]-i[0][0])*(i[2][1]-i[0][1]):
        print('Yes')
        exit()
        
    else:
        continue
print('No')