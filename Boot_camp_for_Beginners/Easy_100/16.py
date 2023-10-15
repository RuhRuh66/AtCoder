N = int(input())
A = list(map(int, input().split()))

ord = enumerate(A, start=1)

ans = [0] * N
for x, y in ord:
    ans[y-1] = x
    
print(*ans)
