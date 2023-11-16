A, B = map(int, input().split())

count = 0
for k in range(A, B+1):
    K = list(str(k))
    judge = all([K[j]==K[-1-j] for j in range((len(K)//2))])
    if judge:
        count += 1
        
print(count)
        


        
            
    