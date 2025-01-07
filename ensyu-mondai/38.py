N, Q = map(int, input().split())
A = [0]+list(map(int, input().split()))

from itertools import accumulate

accum = list(accumulate(A))

for i in range(Q):
    L, R = map(int, input().split())
    print(accum[R]-accum[L-1])
    