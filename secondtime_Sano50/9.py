N = int(input())
cnt = 0

def to_eight(x):
    s = ''
    while x > 0:
        r = x % 8
        x //= 8
        s = str(r) + s
    return s

for i in range(1, N+1):
    
    n = str(i)
    if '7' in n:
        continue
    e = to_eight(i)
    if '7' in e:
        continue
    else:
        cnt += 1
        
print(cnt)