x = int(input())

t = x // 11
d = x % 11

if d == 0:
    ans = 2*t
elif 0 <d <=6:
    ans = 2*t +1
else:
    ans = 2*t + 2
    
print(ans)