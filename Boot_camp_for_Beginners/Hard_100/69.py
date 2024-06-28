N = int(input())
A = []
for i in range(N):
    temp = int(input())
    A.append(temp)

A.sort()

if N % 2 == 0:
    h = N//2
    p1 = A[h]+2*sum(A[h+1:])
    m1 = A[h-1]+2*sum(A[:h-1])
    ans = p1-m1
    
else:
    h = N//2 + 1
    p2 = 2*sum(A[h:])
    m2 = A[h-1]+A[h-2] +2*sum(A[:h-2])
    ans2 = p2-m2
    
    p3 = A[h-1] + A[h] + 2*sum(A[h+1:])
    p4 = 2*sum(A[:h-1])
    ans3 = p3-p4
    
    ans = max(ans2, ans3)
    
print(ans)