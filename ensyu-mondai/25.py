N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = (sum(A)+2*sum(B))/3


print(ans)