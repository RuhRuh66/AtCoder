import itertools


N, K = map(int, input().split())
A = []
for i in range(N):
    a = list((map(int, input().split())))
    A.append(a)
    
import itertools

B = itertools.permutations([k for k in range(1, N)])

