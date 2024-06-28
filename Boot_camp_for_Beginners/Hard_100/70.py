N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

from bisect import bisect_left, bisect_right

ans = 0


for i in range(N):
    s = bisect_right(A, B[i]-1)
    s_n = s
    l = bisect_left(C, B[i]+1)
    l_n = N-l
    
    ans += s_n * l_n
    
print(ans)

