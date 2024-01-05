N = int(input())

A = []
for i in range(N):
    temp = list(map(int, input().split()))

    A.append(temp)


from itertools import combinations

s = combinations(A, 2)

dist = 0
for a, b in s:
    dist += ((a[0]-b[0]) ** 2 + (a[1]-b[1])**2)**0.5

print(dist * 2/N)