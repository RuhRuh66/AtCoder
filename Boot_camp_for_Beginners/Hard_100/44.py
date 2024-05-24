N = int(input())


queries = [[] for i in range(N+1)]


for j in range(N):
    A = int(input())
    for i in range(A):
        x, y = map(int, input().split())
        queries[j+1].append((x,y))

for i in range(1<<N):
    assump = [[] for i in range(N+1)]
    persons = [[] for i in range(N+1)]
    for j in range(N):
        if i>>j & 1 == 1:
            for x, y in queries[j+1]:
                persons[x].append(y)
            assump[j+1].append(1)
        else:
            assump[j+1].append(0)
    print(persons, assump)
    
     
            
