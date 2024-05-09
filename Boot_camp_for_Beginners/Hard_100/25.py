from math import ceil

def estimate(start_time, first_train, interval, cost):
    eta = 0
    if start_time <= first_train:
        eta = first_train + cost
        return eta
    else:
        eta = ceil((start_time - first_train)/interval) * interval + first_train + cost
        return eta
    
    
N = int(input())
TT = []
for _ in range(N-1):
    cost, first_train, interval = map(int, input().split())
    TT.append((cost, first_train, interval))
    
    
for i in range(N-1):
    start_time = 0
    for j in range(i,N-1):
        cost, first_train, interval = TT[j][0], TT[j][1], TT[j][2]
        eta = estimate(start_time, first_train, interval, cost)
        start_time = eta
    print(eta)

        
print(0)
        
    