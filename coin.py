A, B, C, X = [int(input()) for i in range(4)]
X //= 50

count = 0

for i in range(A+1):
    if 10 * i > X:
        break
    rem = X - 10*i
    for j in range(B+1):
        if 2 * j > rem:
            break
        if rem - 2*j <= C:
            count += 1
            
print (count)
