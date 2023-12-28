N = int(input())
A = list(map(int, input().split()))


count = 0
for i in range(N):
    k = A[i]
    while k%2 == 0:
        count+=1
        k //= 2

print(count)

