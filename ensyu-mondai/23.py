N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

ans = (sum(B) + sum(R)) / N
print(ans)