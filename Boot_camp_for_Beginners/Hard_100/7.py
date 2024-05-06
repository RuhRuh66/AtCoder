N, M = map(int, input().split())
A = list(map(int, input().split()))

from heapq import heappushpop, heapify

heapify(A)



for i in range(M):
    b, c = map(int, input().split())
    for j in range(b):
        heappushpop(A, c)

print(sum(A))


    