N = int(input())
A = list(map(int, input().split()))

from collections import deque

sums = sum(A)
if sums % 10 != 0:
    print('No')
    exit()
    
tens = sums//10

temp = 0
p = 0
while temp < tens:
    temp += A[p]
    p += 1
    
A += A[0:p]
    

ans = 0
temp_sum = 0
q = deque()

for i in A:
    q.append(i)
    temp_sum += i
    if temp_sum == tens:
        print('Yes')
        exit()
    
    while q and temp_sum > tens:
        rm = q.popleft()
        temp_sum -= rm
        if temp_sum == tens:
            print('Yes')
            exit()
print('No')


