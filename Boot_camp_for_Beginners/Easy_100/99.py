N, K = map(int, input().split())

if N != 1:
    ans = K * ((K-1) ** (N-1))

    print(ans)
    
else:
    print(K)
N, K = map(int, input().split())

ans = K * (K-1) ** (N-1)

print(ans)