X, K, D = map(int, input().split())

if abs(X) >= K*D:
    ans = abs(X) - K*D
    print(ans)
    exit()

Y = abs(X) // D
if (K -Y) % 2 == 0:
    ans = abs(X) - Y*D
    
else:
    ans = (Y+1)*D - abs(X)
    
print(ans)