N = int(input())


queries = [[] for i in range(N+1)]


for j in range(N):
    A = int(input())
    for i in range(A):
        x, y = map(int, input().split())
        queries[j+1].append((x,y))


ans = 0
for i in range(1<<N):
    assump = [0] * (N+1)
    judge = [[] for _ in range(N+1)] 
   
    for j in range(N):
        if i>>j & 1 == 1:
            assump[j+1] = 1
            for x, y  in queries[j+1]:
                judge[x].append(y)
          
                    
   
    
    for k in range(1, N+1):
        if len(judge[k]) > 1:
           break
        if (assump[k] == 1 and judge[k]== [0]) or (assump[k] == 0 and judge[k] == [1]):
            break
        else:
            temp = assump.count(1)
    
    ans =  max(ans, temp)   
          

print(ans)
                    
                    
                    
# '-----------------------------------   '             
    
    
n = int(input())
li = []
a = []
ans_cnt = 0

for i in range(n):
    a_tmp = int(input())
    x = [list(map(int,input().split())) for _ in range(a_tmp)]
    a.append(a_tmp)
    li.append(x)

for i in range(1<<n):
    cnt = 0
    flg = 0
    ans = [0]*n #仮定した正直者リスト
    for m in range(n):
        if 1&(i>>m):
            ans[m] = 1
        else:
            ans[m] = 0
    for j in range(n):
        if 1&(i>>j):
            for k in range(a[j]):
                if ans[li[j][k][0]-1] != li[j][k][1]:
                    flg = 1
    if flg == 0:
        for l in ans:
            if l == 1:
                cnt+=1
        ans_cnt = max(ans_cnt,cnt)

print(ans_cnt)        
                    
            
            
            
            
    
    
    
    