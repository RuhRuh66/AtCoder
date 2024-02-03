N = int(input())


Sum = 0
SB = 10**9

for i in range(N):
    s = int(input())
    Sum += s
    if s % 10 != 0:
        SB = min(SB, s)
        
        


if Sum % 10 != 0:
    print(Sum)
else:
    if SB == 10 **9:
        print(0)
    else:
        print(Sum - SB)