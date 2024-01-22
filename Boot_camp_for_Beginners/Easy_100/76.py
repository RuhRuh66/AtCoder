N, M = map(int, input().split())

D = [[] for i in range(N)]

for j in range(M):
    p, s = input().split()
    p = int(p) - 1
    D[p].append(s)
    


right_ans = 0
penalty = 0

for k in D:
    flag = False
    if 'AC' in k:
        right_ans += 1
        for l in k:
            if l == 'WA':
                penalty += 1
            else:
                break
    else:
        continue
print(right_ans, penalty)
    

                
        
        


