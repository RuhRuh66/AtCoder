import bisect
import itertools

n, k = map(int, input().split())
a = list(map(int, input().split()))

x = [0] + list(itertools.accumulate(a))

ans = 0

print(x)