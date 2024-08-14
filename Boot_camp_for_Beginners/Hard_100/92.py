N, M = map(int, input().split())

s = [0] * N

for i in range(M):
    a, b = map(int, input().split())

    s[a-1] += 1
    s[b-1] += 1


print('YES' if all([True if s[i]%2 == 0 else False for i in range(N)]) else 'NO')