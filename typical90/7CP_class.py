N = int(input())
A = list(map(int, input().split()))

A.sort()

Q = int(input())

for i in range(Q):
    b = int(input())
    ans = 0
    if b <= A[0]:
        ans = A[0]-b
    elif b >= A[N-1]:
        ans = b - A[N-1]
    else:
        ok = -1
        ng = N
        while ng - ok > 1:
            mid = (ok + ng) //  2
            if b <= A[mid]:
                ng = mid
            else:
                ok = mid
        ans = min(b-A[ok], A[ng]-b) 
    print(ans)
            
        



    
    