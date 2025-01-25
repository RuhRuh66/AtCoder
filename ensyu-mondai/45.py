import sys
n, m = map(int, input().split())
p = [0] * n

for j in range(m):
    a, b = map(int, input().split())
    i = a if a>b else b
    p[i-1] += 1
    
print(sum(1 for i in p if i == 1))
