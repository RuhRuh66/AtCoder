def solve(a, x, m):
    if x == 0:
        return 0
    if x % 2 == 1:
        return (solve(a, x-1, m) + pow(a, x-1, m))%m
    if x % 2 == 0:
        return((1+pow(a, x//2, m))*solve(a, x//2, m))%m
    

A, X, M = map(int, input().split())
print(solve(A, X, M))