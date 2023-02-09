N, K = map(int, input().split())
village = []
for i in range(N):
    A, B = map(int, input().split())
    village.append([A, B])
    
s_village = sorted(village)
pocket = K
for i in range(N):
    if s_village[i][0] <= pocket:
        pocket += s_village[i][1]
        
        
print(pocket)
        

    

        


