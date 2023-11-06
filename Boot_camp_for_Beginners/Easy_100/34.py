A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for i in range(A+1):
    if 500 * i > X:
        break
    else:
        for j in range(B+1):
            if 500 * i + 100 *j >X:
                break
            else:
                for k in range(C+1):
                    if 500*i + 100*j + 50*k > X:
                        break
                    else:
                        if 500*i + 100*j + 50*k == X:
                            count += 1

print(count)                           