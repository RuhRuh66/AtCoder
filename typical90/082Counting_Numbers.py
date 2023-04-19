L, R = map(int, input().split())


mod = 10**9+7

A = len(str(L))
B = len(str(R))


ans = 0
for i in range(A, B+1):
    min_num = max(L, 10**(i-1))
    max_num = min(R, 10**i -1)
    num = max_num - min_num +1
    ans += i * (((min_num + max_num) * num )// 2)

print(int(ans % mod))
    