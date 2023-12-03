N = int(input())
T, A = map(int, input().split())

H = list(map(int, input().split()))

temp = []
for i in range(N):
    temp_i = T - H[i] * 0.006
    dif = abs(A-temp_i)
    temp.append(dif)
    
best = min(temp)

ans = temp.index(best)+1

print(ans)