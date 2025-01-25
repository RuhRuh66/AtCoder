N, Q = map(int, input().split())

dif = [0] *(N-1) #右から左を引いた差分
for i in range(Q):
    L, R, snow = map(int, input().split())
    L, R = L-1, R-1
    
    if L != 0:
        dif[L-1] += snow
    if R != N-1:
        dif[R] -= snow
ans =''
for j in range(N-1):
    if dif[j] == 0:
        ans += '='
    elif dif[j] > 0:
        ans += '<'
    else:
        ans += '>'
        
print(ans)
        
        

