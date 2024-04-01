K, S  =map(int, input().split())

count_3 = 0
for i in range(K+1):
    if i > S:
        break
    for j in range(K+1):
        if i + j > S:
            break
        else:
            if S-(i+j) <= K:
                count_3 += 1
                
print(count_3)

                

                
    