A, B, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_a = min(a)
min_b = min(b)

min_total = min_a+min_b
for i in range(M):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    temp = a[x] + b[y] - c
    min_total = min(min_total, temp)

print(min_total)