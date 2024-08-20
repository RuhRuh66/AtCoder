N = int(input())
dic = {}
for i in range(N):
    s, t = map(str, input().split())
    t = int(t)
    dic[s] = t
    

sorted_mounts = sorted(dic.items(), key= lambda x:x[1], reverse = True)
    
print(sorted_mounts[1][0])   