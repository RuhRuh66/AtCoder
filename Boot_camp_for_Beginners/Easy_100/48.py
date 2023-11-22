N = int(input())

H = list(map(int, input().split()))

count = 0
ans = 0
for i in range(N-1):
    if H[i+1] <= H[i]:
        count += 1
        ans = max(ans, count)
    else:
        count = 0
        
print(ans)