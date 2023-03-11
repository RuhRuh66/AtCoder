import sys
sys.setrecursionlimit(10**6)

N  = int(input())
desitinations = [[] for i in range(N+1)]
for i in range(1, N):
    A, B = map(int, input().split())
    desitinations[A].append(B)
    desitinations[B].append(A)
    
distance = [-1] * (N+1)

def dfs(start, dest, dist):
    for i in dest[start]:
        if dist[i] == -1:
            dist[i] = dist[start] + 1
            dfs(i, dest, dist)
    return dist


if __name__ == '__main__':
    l=dfs(1, desitinations, distance)
    s = l.index(max(l))
    distance2 = [-1] * (N+1)
    distance2[s] = 0
    m = dfs(s, desitinations, distance2)
    print(max(m)+1)
    



    

        



                
        
            
    