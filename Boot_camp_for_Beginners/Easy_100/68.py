N = int(input())
L = []
for i in range(1, N+1):
    city, score = input().split()
    L.append((i, city , int(score)))    


ans = sorted(L, key = lambda x:(x[1], -x[2]))
for j in ans:
    print(j[0])