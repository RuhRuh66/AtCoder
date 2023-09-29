n = int(input())
X = []
Y = []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    
import statistics

med_x = statistics.median(X)
med_y = statistics.median(Y)

ans = 0

for i in range(n):
    ans += abs(med_x-X[i]) + abs(med_y-Y[i])
    
print(int(ans))