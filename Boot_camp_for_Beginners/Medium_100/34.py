N, K = map(int, input().split())
A = list(map(int, input().split()))


from math import ceil

ans = ceil(1+(N-K)/(K-1))

print(ans)