N = int(input())

A = list(map(int, input().split()))
Q = int(input())
         
A_sorted = sorted(A)


for i in range(Q):
    ok = -1
    ng = N
    B = int(input())
    
    if B <= A_sorted[0]:
        ans = A_sorted[0] - B
        print(ans)
        
    elif B >= A_sorted[N-1]:
        ans = B - A_sorted[N-1]
        print(ans)
        
    else:
        while ng-ok >1:
            mid = (ng+ok)//2
            if B >= A_sorted[mid]:
                ok = mid
            else:
                ng = mid
        ans = min(B-A_sorted[ok], A_sorted[ng]-B)
        print(ans)
        
