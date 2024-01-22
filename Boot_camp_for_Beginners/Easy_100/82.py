Q, H, S, D = map(int, input().split())
N = int(input())
N = 4*N

q = 4*Q
h = 2*H
s = S
d = D/2

price = [(q, 1, Q), (h, 2, H) , (s, 4, S),  (d, 8, D)]
price.sort()

ans = 0
for i in price:
    n, m = divmod(N, i[1])
    if n >0:
        ans += n * i[2]
        N = m

print(ans)    
