from heapq import heapify, heappop, heappush


N, M = map(int, input().split())
A = list(map(int, input().split()))

A_minus = [i * (-1) for i in A]

heapify(A_minus)


tickets  = M
while tickets:
    t = heappop(A_minus)
    discounted = ((-1*t)//2) * -1
    heappush(A_minus, discounted)
    tickets -= 1
    
print(sum(A_minus)*(-1))

