N = int(input())
S = str(input())

A = []
count = 1
for i in range(N-1):
    if S[i+1] == S[i]:
        count += 1
    else:
        A.append(count)
        count = 1
A.append(count)

B = 0

def arith_sum(n):
    return (n+1)*n//2

for j in A:
    B += arith_sum(j)
    
print(arith_sum(N)-B)
    




    