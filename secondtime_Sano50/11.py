N, K = map(int, input().split())

now = 0
mon = K

from collections import defaultdict

friends = defaultdict(int)
for i in range(N):
    v, m = map(int, input().split())
    friends[v] += m
    
friends = sorted(list(friends.items()))
f = len(friends)
now = now+K

for i in range(f):
    f_v = friends[i][0]
    f_m = friends[i][1]
    
    if f_v <= now:
        now += f_m
        
    else:
        break

print(now)

    




    
    


    


      
