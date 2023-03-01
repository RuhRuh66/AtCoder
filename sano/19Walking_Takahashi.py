X, K, D = map(int, input().split())

if K * D < abs(X):
    ans = abs(X)-K*D
else:
    A = abs(X) % D
    k = abs(X) // D

    ans = 0
    if X >= 0:
        if (K - k) % 2 == 1:
            ans = A - D
        else:
            ans = A
    else:
        if (K -k) % 2 == 1:
            ans = -A + D
        else:
            ans = -A
        
print(abs(ans))