N = int(input())
A = list(map(int, input().split()))

called = [False] * N

for i in range(N):
    if called[i] == False:
        called[A[i]-1] = True

print(called.count(False))

for j, x in enumerate(called):
    if x == False:
        print(j+1, end = ' ')
