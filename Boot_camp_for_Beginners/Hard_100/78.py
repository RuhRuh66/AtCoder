s = input()
K = int(input())

L = len(s)

lis = set()

for i in range(L):
    for j in range(1, K+1):
        if i+j < L+1:
            lis.add(s[i:i+j])
            
a = sorted(list(lis))

print(a[K-1])
        