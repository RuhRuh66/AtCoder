N = int(input())
A = list(map(int, input().split()))

minus_count = 0
sum = 0
min_num = 10**6
for i in range(N):
    a = A[i]
    if a < 0:
        minus_count += 1
    b = abs(a)
    min_num = min(min_num, b)
    sum += b
    
if minus_count % 2 == 0:
    print(sum)

else:
    print(sum-2*min_num)
    