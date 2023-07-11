k = int(input())

divisors = set()

n = 1
while n**2 <= k:
    if k % n == 0:
        divisors.add(n)
        divisors.add(k//n)
    n += 1
    
s = sorted(divisors)

ans = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        a = s[i]
        b = s[j]
        if a * b > k:
            break
        if k//(a*b) < b:
            break
        if k%(a*b)==0:
            ans += 1
print(ans)
