N = int(input())

ans = []
def dfs(s='a', n=1):
    if len(s) == N:
        ans.append(s)
        return
    else:
        for i in range(n+1):
            if i < n:
                new_n = n
            else:
                new_n = i+1
            dfs(s + chr(ord('a')+i), new_n)

dfs()

print(*ans)

        
        
    
    
    





        
    
    
    