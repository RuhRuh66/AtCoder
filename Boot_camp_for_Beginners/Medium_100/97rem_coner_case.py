N = int(input())

if N == 1:
    print(1)
    exit()
    
if N == 2:
    print(2)
    exit()
        

S = 0
I = 0

for i in range(N):
    S += i
    if S >= N:
        I = i
        break

if S-N == 0:
    for i in range(1, I+1):
        print(i)
else:
    for i in range(1, I+1):
        if i != S-N:
            print(i)