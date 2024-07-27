N = int(input())

F = [int(''.join(input().split()), 2)for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]


# print(F)
ans = - 10 ** 12
for i in range(1, 1<<10):
    temp = 0
    for j in range(N):
        cnt = bin(i & F[j]).count('1')
        temp += P[j][cnt]
    ans = max(ans, temp)

print(ans)