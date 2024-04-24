N = int(input())
S = input()

ans = 0
for i in range(10):
    I = S.find(str(i))
    if I == -1:
        continue
    else:
        for j in range(10):
            J = S.find(str(j), I+1)
            if J == -1:
                continue
            else:
                for k in range(10):
                    K = S.find(str(k), J+1)
                    if K == -1:
                        continue
                    else:
                        ans += 1
                        
print(ans)
    