def solve():
    N = int(input())
    a, b = 1, 1
    for i in range(2, N):
        a, b = b, (a+b) % 1000000007
    return b

print(solve())
    