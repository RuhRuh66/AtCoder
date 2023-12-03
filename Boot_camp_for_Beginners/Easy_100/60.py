N = int(input())
T = list(map(int, input().split()))
M = int(input())

sums = sum(T)

for i in range(M):
    p, x = map(int, input().split())
    print(sums - T[p-1] + x)
    
    