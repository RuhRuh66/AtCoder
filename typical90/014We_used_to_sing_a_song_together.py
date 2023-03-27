N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = sorted(A)
b = sorted(B)

ans =  0
for i in range(N):
    ans += abs(a[i]-b[i])
    
print(ans)