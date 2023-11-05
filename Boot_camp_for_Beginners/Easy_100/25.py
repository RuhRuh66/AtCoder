import itertools

n = int(input())

p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

X = list(itertools.permutations(range(1, n+1), n))

a = X.index(p)
b = X.index(q)

print(abs(a-b))